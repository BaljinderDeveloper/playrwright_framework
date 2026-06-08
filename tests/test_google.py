import re
from playwright.sync_api import expect

def test_google(page):
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button",name="Accept all").click(5000)
    except:
        print("No popup appeared")
        
    page.get_by_role("combobox",name="Search").fill("Firefly")
    page.keyboard.press("Enter")
    
    page.wait_for_timeout(5000)
    expect(page).to_have_title(re.compile("Firefly22",re.IGNORECASE)) 
    # expect waits automaticallyb for title to match
    