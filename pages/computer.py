import re
from playwright.sync_api import Page,expect

class Computer:
    def __init__(self,page:Page):
        self.page = Page
        self.desktop_img = page.locator("//img[@alt='Picture for category Desktops']")
        
    def click_desktop(self):
        self.desktop_img.click()
        
    
        

