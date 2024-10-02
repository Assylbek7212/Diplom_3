from page_objects.base_page import BasePage
from locators.login_locators import StellarBurgersLoginLocators
from locators.home_page_locators import StellarBurgersHomePageLocators
from locators.forgot_password_locators import StellarBurgersForgotPasswordLocators
from config import URL


class LoginPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def open_login_page(self):
        self.navigate(URL.LOGIN.value, StellarBurgersLoginLocators.TITLE_FORM)

    def enter_email(self, email):
        self.enter_test(StellarBurgersLoginLocators.EMAIL, email)

    def enter_password(self, password):
        self.enter_test(StellarBurgersLoginLocators.PASSWORD, password)

    def click_login(self):
        self.action_click(StellarBurgersLoginLocators.BUTTON_LOGIN,
                          StellarBurgersHomePageLocators.CHECKOUT_BUTTON)

    def click_link_forgot_password(self):
        self.action_click(StellarBurgersLoginLocators.LINK_FORGOT_PASSWORD,
                          StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)

    def login(self, email, password):
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
