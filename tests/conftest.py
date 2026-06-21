import pytest
from playwright.sync_api import  APIRequestContext
from pages.login_page import LoginPage
from api.employee_api import EmployeeAPI


# 🆕 ADD THIS FIX TO FORCE BASE_URL VALUE TO PARALLEL WORKERS
@pytest.fixture(scope="session", autouse=True)
def base_url(request):
    """Ensures base_url is never None across xdist parallel workers."""
    url = request.config.getoption("--base-url") or request.config.getini("base_url")
    if not url or url == "None":
        return "https://opensource-demo.orangehrmlive.com"
    return url.strip('"\'') # Clean any trailing quotes if present

# 1. FIXED: Replaced manual sync_playwright() with engine's active 'playwright' driver
@pytest.fixture(scope="session")
def auth_state_fixture(playwright, tmp_path_factory, base_url):
    # Uses the engine's active loop cleanly to launch a session browser without collisions
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(base_url=base_url)
    page = context.new_page()

    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")

    # Save session credentials to temp directory shared across xdist parallel workers
    state_path = tmp_path_factory.mktemp("auth") / "state.json"
    context.storage_state(path=str(state_path))
    
    context.close()
    browser.close()
    return state_path

# 2. FIXED: Injected playwright directly to run safely on worker nodes
@pytest.fixture(scope="function")
def api_context(playwright, auth_state_fixture, base_url) -> APIRequestContext:
    context = playwright.request.new_context(
        base_url=base_url,
        storage_state=str(auth_state_fixture)
    )
    yield context
    context.dispose()

# 3. Exposes the Employee API layer directly to test files
@pytest.fixture(scope="function")
def employee_api(api_context) -> EmployeeAPI:
    return EmployeeAPI(api_context)

# 4. Injects pre-authenticated browser window to test files
@pytest.fixture(scope="function")
def logged_in_page(browser, auth_state_fixture, base_url):
    context = browser.new_context(
        base_url=base_url,
        storage_state=str(auth_state_fixture)
    )
    page = context.new_page()
    yield page
    context.close()