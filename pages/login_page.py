from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self):
        self.page.goto("/web/index.php/auth/login")

    def login(self, username: str, password: str):
        # Action methods should ONLY interact with elements, not assert success outcomes
        if username:
            self.page.get_by_placeholder("Username").fill(username)
        if password:
            self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
    
    def get_error_message(self):
        return self.page.get_by_text("Invalid credentials")