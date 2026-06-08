import re
import pytest
from playwright.sync_api import Page,expect
from pages.dashboard import Dashboard
from pages.homepage import Homepage

def get_testdata_json()->list:
    import json
    with open ("./test_data/test_1_verify_login.json","r") as file:
        data = json.load(file)
    return [
        (item["username"], item["password"])
        for item in data
    ]
        
@pytest.mark.parametrize("username,password",get_testdata_json())
def test_verify_login(page: Page,username,password) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    
    dashboard_obj = Dashboard(page)
    homepage_obj = Homepage(page)
    
    # Step1: login
    homepage_obj.verify_register_link_visible()
    homepage_obj.login(username,password)
    print("Step1: login to Demo WorkShop - passed")
    
    # Step2: verify user is logged in
    dashboard_obj.verify_logout()
    print("Step2: login to Demo WorkShop - passed")
    