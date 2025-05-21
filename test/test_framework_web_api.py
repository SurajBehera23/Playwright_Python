import json
import time
import pytest
from pathlib import Path
from playwright.sync_api import Playwright

from page_objects.login import LoginPage
from utils.api_base_framework import APIutils

file_path = Path(__file__).parent.parent / "data" / "credentials.json"

with open(file_path) as f:
    test_data = json.load(f)

user_credential_list = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credential_list)
def test_web_api(playwright: Playwright, user_credentials, browser_instance, app_url):
    user_name = user_credentials["userEmail"]
    user_password = user_credentials["userPassword"]
    #Creates order from API
    api_utils = APIutils()
    order_id = api_utils.create_order(playwright, user_credentials)
    #UI flow
    login = LoginPage(browser_instance, app_url)
    login.navigate()
    dashboard = login.login(user_name, user_password)
    order_history = dashboard.select_orders_link()
    order_history.view_order(order_id)
    time.sleep(5)
