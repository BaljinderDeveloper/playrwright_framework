# # the name starts with test_*.py.  <- to make use of pytest
# # 
# from playwright.sync_api import sync_playwright

# def test_google_title():
#     with sync_playwright() as p:
#         # Launch browser
#         browser = p.chromium.launch(headless=False)

#         # Create a new page
#         page = browser.new_page()

#         # Navigate to Google
#         page.goto("https://www.google.com")

#         # Verify the title
#         assert "Google" in page.title()

#         # Close the browser
#         browser.close()
        
