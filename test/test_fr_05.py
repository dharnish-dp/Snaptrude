from page import LoginPage  
import inspect
from utils import *

def test_FR05(page):  # page fixture from conftest.py
    
    # Login To Application
    login_page = LoginPage(page)  
    login_page.login() 
    login_page.is_login_successful()
    dashboard_page  = login_page.navigate_to_dashboard()
    
    # Create To WorkSpace
    dashboard_page.create_new_project("test5","mm")
    dashboard_page.verify_work_space_is_empty()
    workspace_page = dashboard_page.navigate_to_workpage()
      
    # Draw Rectangle of random width
    workspace_page.select_rectangle_under_freeform()
    workspace_page.create_rectangle(inspect.currentframe().f_code.co_name, 100)
    capital_value = workspace_page.get_capital_area_value()
    workspace_page.select_pointer_mode()
    workspace_page.select_copy_mode()
    workspace_page.replicate_rectangle() # For Now replicate 3 times
    workspace_page.select_pointer_mode()
    capital_value1 = workspace_page.get_capital_area_value() 
    assert int(float(capital_value)*4) == int(float(capital_value1)) # Verify capital area is increase based on increment of rectangle area
    