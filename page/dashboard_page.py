from playwright.sync_api import expect
from utils import *

class DashBoardpage:
    def __init__(self, page):
        self.page = page
        
        # Locator of DashBoardPage
        self.new_project_selector = ("button", "New Project")
        self.text_box_field_selector = ("textbox", "Enter the name of the project")
        self.create_btn_selector = ("button", "Create")
        self.project_title = "#project-title"
        self.design_mode = ("img","pointer")
        self.capital_area = "#area-sidebar-chart"
        self.verify_login_page = "span"
        self.personal_work_space = "#drop_personal_root"
        self.project_card = "link"
        self.setting_btn = ("button", "folder")
        self.delete_btn1 = "Delete"
        self.delete_btn2 = ("button", "Delete")
        self.avatar = ("img", "avatar")
        self.logout_btn = "Logout"
        
         
         
    # Create Project
    def create_new_project(self, project_name, dimention):
        self.page.get_by_role(self.new_project_selector[0], name=self.new_project_selector[1], exact=False).click()
        self.page.get_by_role(self.text_box_field_selector[0], name=self.text_box_field_selector[1], exact=False).fill(project_name)
        self.page.get_by_text(dimention).click()
        self.page.get_by_role(self.create_btn_selector[0], name=self.create_btn_selector[1], exact=False).click()
        expect(self.page.locator("#project-title")).to_contain_text(project_name)
        logger.info("Created the new project")
        
        
    # Verify Work Space is empty
    def verify_work_space_is_empty(self):
        self.page.get_by_role(self.design_mode[0], name=self.design_mode[1]).click()
        expect(self.page.locator(self.capital_area)).to_contain_text("No builtform1000")
        logger.info("Verify Work Space is empty")
        
        
    # Navigate to workspace page
    def navigate_to_workpage(self):
        from page import WorkSpacePage
        workspace_page = WorkSpacePage(self.page)
        return workspace_page
    
    
    # Navigate to Dashboard Page
    def navigate_dashboard_page(self):
        self.page.goto(Setting.DASHBOARD_URL)
        expect(self.page.locator(self.personal_work_space)).to_contain_text("Personal")
        logger.info("Navigated to Dashboard")
    
    
    # Delete Project
    def delete_project(self):   
        try:
            # Hover over the first "Edited" link
            element = self.page.get_by_role(self.project_card, name=re.compile(".*Edited.*")).first
            element.hover()
            
            # Click the folder button
            folder_button = self.page.get_by_role(self.setting_btn[0], name=self.setting_btn[1], exact=True)
            folder_button.wait_for(timeout=5000)  # Wait for the button to be available
            folder_button.click()
            
            # Click "Delete"
            delete_option = self.page.get_by_text(self.delete_btn1)
            expect(delete_option).to_be_visible()
            delete_option.click()
            
            # Confirm the deletion
            delete_button = self.page.get_by_role(self.delete_btn2[0], name=self.delete_btn2[1])
            delete_button.wait_for(timeout=5000)  # Wait for the button to be available
            delete_button.click()
            logger.info("Deleted Project")
            
        except:
            logger.error('Failed to delete work environment')
    
    # Log Out form the platform
    def logout(self):
        self.page.get_by_role(self.avatar[0], name=self.avatar[1]).click()
        self.page.get_by_text(self.logout_btn).click()
        expect(self.page.locator(self.verify_login_page)).to_contain_text("Sign In")
        logger.info("Logged out from platform")  
        
        
        
    
    
        