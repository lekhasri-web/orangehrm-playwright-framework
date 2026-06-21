from playwright.sync_api import Page, expect
from pages.leave_page import LeavePage

def test_leave_list_loads(logged_in_page: Page):
    leave = LeavePage(logged_in_page)
    leave.goto()
    leave.is_leave_page_loaded()

def test_leave_page_has_filter(logged_in_page: Page):
    leave = LeavePage(logged_in_page)
    leave.goto()
    expect(logged_in_page.get_by_role("button", name="Search")).to_be_visible()