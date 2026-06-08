import re
from playwright.sync_api import Page,expect

class Homepage:
    def __init__(self,page:Page):
        self.page = page
        self.register_link = page.locator("//a[contains(text(),'Register')]")
        self.login_page = page.get_by_role("link", name="Log in")
        self.username_input = page.get_by_role("textbox", name="Email:")
        self.password_input = page.get_by_role("textbox", name="Password:")
        self.login_button = page.get_by_role("button", name="Log in")
        self.logout_link = page.get_by_role("link", name="Log out")
        
    def enter_username(self, username:str):
        self.username_input.fill(username)
        
    def enter_password(self,password:str):
        self.password_input.fill(password)
        
    def click_login(self):
        self.login_button.click()
        
    def verify_register_link_visible(self):
        expect(self.register_link).to_be_visible()
        
    def login(self, username:str, password:str):
        self.login_page.click()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
        