import re
from playwright.sync_api import Page,expect

class Dashboard:
    def __init__(self,page:Page):
        self.page = page
        self.logout_link = page.get_by_role("link", name="Log out")
    
    def verify_logout(self):
        expect(self.logout_link).to_be_visible()
    
    