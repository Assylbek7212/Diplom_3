from page_objects.base_page import BasePage
from locators.register_locators import StellarBurgersRegister
from locators.login_locators import StellarBurgersLoginLocators
from config import URL


class RegisterPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def open_register_page(self):
        self.navigate(URL.REGISTER.value, StellarBurgersRegister.EMAIL)

    def enter_name(self, name):
        self.enter_test(StellarBurgersRegister.NAME, name)

    def enter_email(self, email):
        self.enter_test(StellarBurgersRegister.EMAIL, email)

    def enter_password(self, password):
        self.enter_test(StellarBurgersRegister.PASSWORD, password)

    def click_register(self):
        self.action_click(StellarBurgersRegister.SUBMIT_BUTTON,
                          StellarBurgersLoginLocators.TITLE_FORM)

    def signup(self, name, email, password):
        self.open_register_page()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register()
