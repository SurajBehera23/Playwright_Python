import os
import shutil
import pytest
from playwright.sync_api import Playwright

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    report_dir = os.path.join(root_dir, "report")

    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)

    os.makedirs(report_dir)

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome | firefox | webkit"
    )
    parser.addoption(
        "--app_url",
        action="store",
        default="https://rahulshettyacademy.com/client/",
        help="Base URL of the application under test"
    )

@pytest.fixture(scope="session")
def app_url(request):
    return request.config.getoption("app_url")

@pytest.fixture(scope="function")
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def user_credentials(request):
    return request.param
