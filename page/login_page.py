import os
from utils import *
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        
        # Locators
        self.verify_login_page = "span"
        self.username_selector = ("textbox","username@company.com")
        self.password_selector = "input[type='password']"
        self.login_btn_selector = ("button","Sign In")
        self.personal_work_space = "#drop_personal_root"
        
    
    # Login to the platform
    def login(self):
        self.page.goto(Setting.ROOT_URL)
        self.page.wait_for_load_state("load") 
        logger.info('Navigated to Home Page') 
        
        # Login to platform   
        expect(self.page.locator(self.verify_login_page)).to_contain_text("Sign In")  
        self.page.get_by_role(self.username_selector[0], name=self.username_selector[1]).click()
        self.page.get_by_role(self.username_selector[0], name=self.username_selector[1]).fill(Setting.USER_NAME)
        self.page.locator(self.password_selector).click()
        self.page.locator(self.password_selector).fill(Setting.PASSWORD)
        self.page.get_by_role(self.login_btn_selector[0], name=self.login_btn_selector[1]).click()
        
        # Verify Login
        expect(self.page.locator(self.personal_work_space)).to_contain_text("Personal")
        logger.info('Loggined to platform') 
    
    
    # Verify login successfull
    def is_login_successful(self):
        self.page.wait_for_url(Setting.DASHBOARD_URL, timeout=30000)
        current_url = self.page.url
        assert current_url == Setting.DASHBOARD_URL # Confirm in dashboard url
        logger.info('In DashBoard Page')
    
    
    # Navigate to DashboardPage
    def navigate_to_dashboard(self):
        from page import DashBoardpage
        dashboard_page = DashBoardpage(self.page)
        return dashboard_page
        
        
        
        
