# page_objects/forgot_password_page.py
import allure
from page_objects.base_page import BasePage
from locators.forgot_password_locators import StellarBurgersForgotPasswordLocators
from config import URL


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        """Переход на страницу восстановления пароля"""
        self.navigate(URL.FORGOT_PASSWORD.value, StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step("Ввод email для восстановления пароля: {email}")
    def enter_email(self, email):
        """Ввод email в поле восстановления пароля"""
        self.enter_text(StellarBurgersForgotPasswordLocators.EMAIL, email)

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_button_restore_password(self):
        """Клик по кнопке 'Восстановить пароль' на странице восстановления пароля"""
        self.action_click(StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)
