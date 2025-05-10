import os
from dotenv import load_dotenv
load_dotenv()

class Setting:
    ROOT_DIR = os.getcwd()
    ROOT_URL = "https://app.snaptrude.com/login"
    DASHBOARD_URL = "https://app.snaptrude.com/dashboard"
    USER_NAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    
    
    