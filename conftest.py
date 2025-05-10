import pytest
from playwright.sync_api import sync_playwright
from utils import *
from page import DashBoardpage
import os


# Read Browser from terminal
def pytest_addoption(parser):
    """Add a command-line option to select the browser."""
    parser.addoption(
        "--test-browser",  # Renamed to avoid conflicts
        action="store", 
        default="chromium", 
        choices=["chromium", "firefox", "webkit"], 
        help="Choose the browser to run tests on"
    )


# Creating playwright Object
@pytest.fixture(scope="function")
def playwright():
    """Fixture to launch Playwright synchronously and provide a browser context."""
    with sync_playwright() as p:
        yield p


# Creating Browser Based On params
@pytest.fixture(scope="function")
def browser(playwright, request):
    """Fixture to launch the selected browser synchronously before each test."""
    browser_choice = request.config.getoption("--test-browser")  # Renamed to match the new option name
    test_name = request.node.name
    logger.info(f'Running test: {test_name}')
    browser = getattr(playwright, browser_choice).launch(headless=False, slow_mo=1000)  # Dynamically select the browser
    yield browser
    browser.close()


# Creating new Context
@pytest.fixture(scope="function")
def context(browser):
    """Fixture to create a new browser context synchronously before each test."""
    context = browser.new_context()
    yield context
    context.close()


# Creating page on new Context
@pytest.fixture(scope="function")
def page(context,request):
    """Fixture to create a new page (tab) in the browser context synchronously before each test."""
    
    # Create a directory for traces if it doesn't exist
    trace_dir = os.path.join(Setting.ROOT_DIR,"traces")
    os.makedirs(trace_dir, exist_ok=True)

    # Get the test name for trace file
    test_name = request.node.name
    trace_file = os.path.join(trace_dir,f"{test_name}.zip")
    # Start tracing
    context.tracing.start(
        snapshots=True,
        screenshots=True,
        sources=True,
    )
    
    page = context.new_page()
    yield page
    
    context.tracing.stop(path=str(trace_file))
    
    # Clean up after each test
    dashboard_page = DashBoardpage(page)
    dashboard_page.navigate_dashboard_page()
    dashboard_page.delete_project()
    dashboard_page.logout()
    page.close()
