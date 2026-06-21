import uuid
from playwright.sync_api import Page, expect
from pages.pim_page import PIMPage

def test_hybrid_search_newly_created_employee(logged_in_page: Page, employee_api):
    """
    SDET Pattern: Seeds data via API instantaneously, 
    then uses UI Page Objects to validate layout visibility.
    """
    # 1. Generate unique details and seed employee via backend API in milliseconds
    unique_id = str(uuid.uuid4())[:8]
    first_name = f"Automation_{unique_id}"
    last_name = "QA"
    
    employee_api.create_employee(first_name, last_name, unique_id)

    # 2. Open UI and interact using Page Objects
    pim = PIMPage(logged_in_page)
    pim.goto()
    
    # 3. Assert the seeded data appears perfectly on the screen
    pim.search_employee(first_name)
    pim.is_employee_present(first_name)