import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
token=os.getenv("API_TOKEN")

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
    

# @pytest.fixture
# def api_context(playwright):
#     token = os.getenv("API_TOKEN")

#     context = playwright.request.new_context(
#         extra_http_headers={
#             "Accept": "application/json",
#             "Authorization": f"Bearer {token}"
#         }
#     )
#     yield context
#     context.dispose()



###################Screenshot fixture###############
import pytest
from datetime import datetime

# Hook to track test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Store test result in item for later use
    setattr(item, "rep_" + rep.when, rep)


# Fixture to take screenshot on failure
@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield

    # Execute only after test execution (teardown phase)
    if request.node.rep_call.failed:
        page = request.node.funcargs.get("page")

        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = request.node.name
            file_name = f"screenshots/{test_name}_{timestamp}.png"

            page.screenshot(path=file_name)
            print(f"\n📸 Screenshot saved: {file_name}")