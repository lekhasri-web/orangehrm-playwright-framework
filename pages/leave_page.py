from playwright.sync_api import Page, expect

class LeavePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/web/index.php/leave/viewLeaveList")

    def is_leave_page_loaded(self):
        expect(self.page.get_by_role("heading", name="Leave List")).to_be_visible()