from utils import *
from playwright.sync_api import expect
import os
import platform

class WorkSpacePage:
    def __init__(self, page):
        self.page = page
        
        # Locator of DashBoardPage
        self.rectangle_selector = ("img", "rectangle")
        self.rectangle_freeform = ("img", "Free Form")
        self.rectangle_verify = "#div-top-menu-bar-rectangle"
        self.canva_selector = "#canvas"
        self.capital_area_locator = "#area-sidebar-chart"
        self.design_mode = ("img","pointer")
        self.capital_area_btn = ("img","Areas")
        self.properties = "Properties"
        self.cope = ("img", "copy")
        
    
    # Select Rectangle Under 
    def select_rectangle_under_freeform(self):
        self.page.get_by_role(self.rectangle_selector[0], name=self.rectangle_selector[1]).click()
        self.page.get_by_role(self.rectangle_freeform [0], name=self.rectangle_freeform[1]).click()
        self.page.get_by_role(self.rectangle_selector[0], name=self.rectangle_selector[1]).click()
        expect(self.page.locator(self.rectangle_verify)).to_be_visible()
        logger.info('Selected rectangle')
    
    
    # Create_rectangle
    def create_rectangle(self,test_name,dimention=100):
        element = self.page.locator(self.rectangle_verify)
        bounding_box = element.bounding_box()
        if bounding_box:
            x, y, width, height = bounding_box.values()
            logger.info(f"Coordinates of #div-top-menu-bar-rectangle:")
            logger.info(f"X: {x}, Y: {y}, Width: {width}, Height: {height}")
        else:
            logger.info("Element not found.")
        self.dimention = dimention
        self.x1,self.y1 = x,y+200
        self.x2,self.y2 = self.x1+dimention,self.y1+dimention
        self.page.locator(self.rectangle_verify).click()
        self.page.locator(self.canva_selector).click(position={"x":self.x1,"y":self.y1})
        self.page.locator(self.canva_selector).click(position={"x":self.x2,"y":self.y2})
        self.screenshot_path = "screenshot"
        os.makedirs(self.screenshot_path, exist_ok=True)
        self.screenshot_path = os.path.join(self.screenshot_path,f"{test_name}.png")
        self.page.screenshot(path=self.screenshot_path, clip={"x": self.x1, "y": self.y1, "width": dimention, "height": dimention})
        logger.info("Created the Rectangle")
        
            
    # Select Point And Capital Area
    def select_pointer_mode(self):
        self.page.get_by_role(self.design_mode[0], name=self.design_mode[1]).click()
        logger.info("Selected Pointer")
    
    
    # Click the rectangle
    def select_rectangle(self):
        self.page.locator(self.canva_selector).click(position={"x":self.x1+(self.dimention//2),"y":self.y1+(self.dimention//2)})
        expect(self.page.get_by_text(self.properties)).to_be_visible()
        logger.info("Selected Rectangle")
        
        
    # Verify rectangle dimention match with capital Area
    def verify_rectangle_dimension(self):
        rectangle_dimention = extract_decimal_from_image(self.screenshot_path)
        if rectangle_dimention is not None:
            expect(self.page.locator(self.capital_area_locator)).to_contain_text(f"{rectangle_dimention}")
        else:
            assert rectangle_dimention is not None, "Rectangle dimension not found!"
        logger.info("Verify the rectangle dimension")
    
    
    # Verify Rectangle dimention is mm
    def verify_rectangle_dimension_cm(self):
        expect(self.page.locator("#object_properties_panel").get_by_text("cm").first).to_be_visible()
        logger.info("Verify the rectangle dimension is cm")
    
    
    # Select the Copy mode
    def select_copy_mode(self):
        self.page.get_by_role("img", name="copy").click()
        logger.info("Selected copy mode")
    
    
    # Replicate Rectangle 
    def replicate_rectangle(self):
        start = self.x1+(self.dimention//2)
        end = self.y1+(self.dimention//2)

        # First Copy
        self.page.locator(self.canva_selector).click(position={"x":start,"y":end})
        self.page.locator(self.canva_selector).click(position={"x":start+200,"y":end})
        
        # Second Copy
        self.page.locator(self.canva_selector).click(position={"x":start,"y":end})
        self.page.locator(self.canva_selector).click(position={"x":start,"y":end+200})
        
        # Third Copy
        self.page.locator(self.canva_selector).click(position={"x":start,"y":end})
        self.page.locator(self.canva_selector).click(position={"x":start+200,"y":end+200})
        logger.info("Replicated the rectangle")
    
    
    # Get Capital value
    def get_capital_area_value(self):
        element_text = self.page.locator("#area-sidebar-chart").text_content()
        # Extract only the area value
        match = re.search(r"(\d+\.\d+)\s*m²", element_text)
        area = None
        if match:
            area = match.group(1)
        return area
    
    # Undo Operation
    def undo_last_action(self):
        # Check the operating system and use the appropriate shortcut
        if platform.system() == "Darwin":  # Mac
            self.page.keyboard.press('Meta+Z')  # Use Meta (Command key on Mac)
        else:  # Windows/Linux
            self.page.keyboard.press('Control+Z')  # Windows/Linux uses Control + Z

        
        
                
        
        
        
    
    
    
    
    
        