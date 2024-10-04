import allure
from page_objects.base_page import BasePage
from locators.forgot_password_locators import StellarBurgersForgotPasswordLocators
from config import URL
from helpers import get_faker_user


class ForgotPasswordPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        """Переход на страницу восстановления пароля"""
        self.navigate(URL.FORGOT_PASSWORD.value, StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step("Ввод email для восстановления пароля")
    def enter_email(self):
        """Ввод email в поле восстановления пароля"""
        self.enter_test(StellarBurgersForgotPasswordLocators.EMAIL, get_faker_user()["email"])

    @allure.step("Клик по кнопке восстановления пароля")
    def click_button_restore_password(self):
        """Клик по кнопке 'Восстановить пароль' на странице восстановления пароля"""
        self.action_click(StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD,
                          StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)
