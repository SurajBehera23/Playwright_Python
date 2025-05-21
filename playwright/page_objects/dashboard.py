from page_objects.base_page import BasePage
from page_objects.orders_history import OrderHistoryPage
from locators.dashboard_page_locators import DashboardPageLocators

class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locators = DashboardPageLocators()

    def select_orders_link(self):
        self.page.locator(self.locators.ORDERS_LINK).click()
        return OrderHistoryPage(self.page)