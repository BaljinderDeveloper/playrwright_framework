import re
import pytest
from playwright.sync_api import Page,expect
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from utils.logger import get_logger
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

logger = get_logger()

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
    logger.info("Starting script execution")
    page.goto(BASE_URL)
    logger.info("Navigated to the URL")
    
    dashboard_obj = Dashboard(page)
    homepage_obj = Homepage(page)
    
    # Step1: login
    homepage_obj.verify_register_link_visible()
    homepage_obj.login(username,password)
    page.screenshot(path="reports/screenshot_step1.png")
    print("Step1: login to Demo WorkShop - passed")
    logger.info("User is logged in..")
    
    # Step2: verify user is logged in
    dashboard_obj.verify_logout()
    print("Step2: login to Demo WorkShop - passed")
    logger.info("User verified that the user is logged in...")
    