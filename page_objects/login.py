from page_objects.base_page import BasePage
from page_objects.dashboard import DashboardPage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    def __init__(self, page, app_url: str):
        super().__init__(page)
        self.app_url = app_url
        self.locators = LoginPageLocators()

    def navigate(self):
        super().navigate_to(self.app_url)

    # Fills the logIn form
    def login(self, user_email: str, user_password: str):
        self.page.wait_for_selector(self.locators.EMAIL_INPUT)
        self.page.locator(self.locators.EMAIL_INPUT).fill(user_email)
        self.page.locator(self.locators.PASSWORD_INPUT).fill(user_password)
        self.page.locator(self.locators.LOGIN_BUTTON).click()
        return DashboardPage(self.page)