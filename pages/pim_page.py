from playwright.sync_api import Page, expect  # Fixed package import typo

class PIMPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/web/index.php/pim/viewEmployeeList")
    
    def search_employee(self, employee_name: str):
        # Tip: Type for hints input sometimes needs a slight delay or wait for network idle if it auto-suggests
        self.page.get_by_placeholder("Type for hints...").first.fill(employee_name)
        self.page.get_by_role("button", name="Search").click()

    def get_employee_row(self, name: str):
        return self.page.get_by_role("row", name=name)

    def is_employee_present(self, name: str):
        expect(self.get_employee_row(name)).to_be_visible()

    def add_employee(self, first_name: str, last_name: str):
        self.page.get_by_role("button", name="Add").click()
        # Fixed: Added 'self.page.' context to the locators below
        self.page.get_by_placeholder("First Name").fill(first_name) 
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully Saved")).to_be_visible()