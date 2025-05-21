import os
import shutil
import pytest
from playwright.sync_api import Playwright
from pytest_html import extras


# Clean and configure report directory
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    report_dir = os.path.join(root_dir, "report")
    config.stash['report_dir'] = report_dir

    # Clean old report directory
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
    os.makedirs(report_dir)

    # Inject HTML report settings
    config.option.htmlpath = os.path.join(report_dir, "test_report.html")
    config.option.self_contained_html = True


# Custom CLI options
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


# Application base URL fixture
@pytest.fixture(scope="session")
def app_url(request):
    return request.config.getoption("app_url")


# Playwright browser instance fixture
@pytest.fixture(scope="function")
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name").lower()

    headless = True  # Force headless in CI

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


# Parametrized credentials fixture
@pytest.fixture(scope="function")
def user_credentials(request):
    return request.param


# Screenshot on failure (pytest-html compatible)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get('browser_instance')
        if page:
            report_dir = item.config.stash['report_dir']
            screenshot_name = f"failure_screenshot_{item.name}.png"
            screenshot_path = os.path.join(report_dir, screenshot_name)

            # Take screenshot and attach
            page.screenshot(path=screenshot_path)
            extra_image = extras.image(screenshot_path, mime_type='image/png', extension='png')

            if hasattr(report, 'extras'):
                report.extras.append(extra_image)
            else:
                report.extras = [extra_image]