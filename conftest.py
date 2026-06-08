import pytest
from playwright.sync_api import sync_playwright

##### fixture = reusable code which sets up before test & cleans up after test

######## browser fixture
#it starts the browser, once per session
#yield lets the test use the browser
#when tests are done then, the browser is closed
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
   
######### page fixture
#uses the browser fixture
#creates a new browser page for each test
#yeild page gives the test a fresh tab
#after test it closes the tab
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
    

