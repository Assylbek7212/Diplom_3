from page_objects.base_page import BasePage
from locators.forgot_password_locators import StellarBurgersForgotPasswordLocators
from locators.reset_password_locators import StellarBurgersResetPasswordLocators
from config import URL
from helpers import get_faker_user


class ForgotPasswordPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def open_forgot_password_page(self):
        self.navigate(URL.FORGOT_PASSWORD.value, StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)

    def click_button_restore_password(self):
        self.action_click(StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD,
                          StellarBurgersResetPasswordLocators.PASSWORD)

    def enter_email(self):
        self.enter_test(StellarBurgersForgotPasswordLocators.EMAIL, get_faker_user()["email"])


