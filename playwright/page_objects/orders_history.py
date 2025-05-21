from page_objects.base_page import BasePage
from locators.orders_history_page_locators import OrderHistoryPageLocators

class OrderHistoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locators = OrderHistoryPageLocators()

    def view_order(self, order_id_from_api):
        row = self.page.locator(self.locators.ORDER_ROW).filter(has_text=order_id_from_api)
        row.get_by_role("button").filter(has_text=self.locators.VIEW_BUTTON_TEXT).click()

        self.page.wait_for_selector(self.locators.ORDER_SUMMARY_TEXT)

        order_id_ui = self.page.locator(self.locators.ORDER_ID_UI).text_content()

        print(f"UI Order ID: {order_id_ui}")
        print(f"API Order ID: {order_id_from_api}")

        assert order_id_ui.strip() == order_id_from_api, f"Order ID mismatch: UI={order_id_ui}, API={order_id_from_api}"