from page import LoginPage  
import inspect

def test_FR02(page):  # page fixture from conftest.py
    
    # Login To Application
    login_page = LoginPage(page)  
    login_page.login() 
    login_page.is_login_successful()
    dashboard_page  = login_page.navigate_to_dashboard()
    
    # Create To WorkSpace
    dashboard_page.create_new_project("test2","mm")
    dashboard_page.verify_work_space_is_empty()
    workspace_page = dashboard_page.navigate_to_workpage()
      
    # Draw Rectangle of random width
    workspace_page.select_rectangle_under_freeform()
    workspace_page.create_rectangle(inspect.currentframe().f_code.co_name, 100)
    workspace_page.select_pointer_mode()
    workspace_page.verify_rectangle_dimension() # Verify Rectangle Dimention match with capital Area
    
    
