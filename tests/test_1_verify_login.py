import re
import pytest
from playwright.sync_api import Page,expect
from pages.dashboard import Dashboard
from pages.homepage import Homepage
from pages.computer import Computer
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def test_verify_login(page: Page) -> None:
    # page.goto("https://demowebshop.tricentis.com/")
    page.goto(BASE_URL)
    
    dashboard_obj = Dashboard(page)
    homepage_obj = Homepage(page)
    computer_obj = Computer(page)
    
    # Step1: login
    homepage_obj.verify_register_link_visible()
    homepage_obj.login("baljinder.tester@gmail.com","Jungle@123")
    print("Step1: login to Demo WorkShop - passed")
    
    # Step2: verify user is logged in
    dashboard_obj.verify_logout()
    print("Step2: login to Demo WorkShop - passed")
    
    #Step3:Goto computers
    homepage_obj.click_computer_dropdown()
    computer_obj.click_desktop()
    print("Step3: clicked on computer")
    
    page.screenshot(path="reports/screenshot.png")
    
    page.wait_for_timeout(5000)  # 5 seconds
    
    