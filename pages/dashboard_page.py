from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def is_loaded(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()

    def navigate_to_pim(self):
        self.page.get_by_role("link", name="PIM").click()

    def navigate_to_leave(self):
        self.page.get_by_role("link", name="Leave").click()