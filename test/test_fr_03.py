from page import LoginPage  
import inspect
from utils import *

def test_FR03(page):  # page fixture from conftest.py
    
    # Login To Application
    login_page = LoginPage(page)  
    login_page.login() 
    login_page.is_login_successful()
    dashboard_page  = login_page.navigate_to_dashboard()
    
    # Create To WorkSpace
    dashboard_page.create_new_project("test3","mm")
    dashboard_page.verify_work_space_is_empty()
    workspace_page = dashboard_page.navigate_to_workpage()
      
    # Draw Rectangle of random width
    workspace_page.select_rectangle_under_freeform()
    workspace_page.create_rectangle(inspect.currentframe().f_code.co_name, 100)
    workspace_page.select_pointer_mode()
    workspace_page.select_copy_mode()
    workspace_page.replicate_rectangle() # For Now replicate 4 times
    capital_value = workspace_page.get_capital_area_value()
    workspace_page.select_pointer_mode()
    if capital_value is not None and capital_value!=0:
        for _ in range(4):
            workspace_page.undo_last_action() # Remove all the rectangle from workspace
        dashboard_page.verify_work_space_is_empty() # Verify capital is empty
    else:
        assert False, "Fail to get capital area"
    