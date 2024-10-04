import allure
from page_objects.base_page import BasePage
from locators.reset_password_locators import StellarBurgersResetPasswordLocators
from helpers import get_faker_user


class ResetPasswordPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("Ввод нового пароля")
    def enter_password(self):
        """Ввод нового пароля в поле ввода"""
        self.enter_test(StellarBurgersResetPasswordLocators.PASSWORD, get_faker_user()["password"])

    @allure.step("Получение атрибута 'type' для поля пароля")
    def get_attribute_password(self):
        """Получение значения атрибута 'type' у поля пароля для проверки типа (текст или пароль)"""
        return str(self.driver.find_element(*StellarBurgersResetPasswordLocators.PASSWORD).get_attribute("type"))

    @allure.step("Клик по кнопке 'Показать/Скрыть' для пароля")
    def click_button_action_password(self):
        """Клик по кнопке для изменения видимости пароля и ожидание обновления поля"""
        self.action_click(StellarBurgersResetPasswordLocators.BUTTON_ACTION_PASSWORD,
                          StellarBurgersResetPasswordLocators.PASSWORD)
