import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Log in").click()
    
    page.get_by_role("textbox", name="Email:").fill("baljinder.tester@gmail.com")
    
    page.get_by_role("textbox", name="Password:").fill("Jungle@123")
    page.get_by_role("button", name="Log in").click()
    expect(page.get_by_role("link", name="Log out")).to_be_visible()

