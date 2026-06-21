from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
 
def test_login_valid_credentials(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")
    expect(page).to_have_url("/web/index.php/dashboard/index")

def test_login_invalid_credentials(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "wrongpassword")
    expect(login.get_error_message()).to_be_visible()

def test_empty_username(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("", "admin123")
    expect(page.get_by_text("Required")).to_be_visible()