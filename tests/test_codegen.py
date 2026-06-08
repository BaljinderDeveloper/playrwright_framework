import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email:").click()
    page.get_by_role("textbox", name="Email:").fill("baljinder.developer@gmail.com")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Lampyridae@4me")
    page.get_by_role("button", name="Log in").click()
    expect(page.get_by_text("Login was unsuccessful. Please correct the errors and try again. The")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
