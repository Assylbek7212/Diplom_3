import allure
from page_objects.base_page import BasePage
from locators.personal_area_locators import StellarBurgersPersonalArea
from locators.login_locators import StellarBurgersLoginLocators
from config import URL

class PersonalArea(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("Клик по кнопке выхода из личного кабинета")
    def click_button_exit(self):
        """Клик по кнопке 'Выход' на странице личного кабинета"""
        self.action_click(StellarBurgersPersonalArea.BUTTON_EXIT,
                          StellarBurgersLoginLocators.TITLE_FORM)

    @allure.step("Проверка, что произошел успешный выход на страницу логина")
    def is_logged_out(self):
        """Проверяет, что после выхода отображается форма логина"""
        return self.wait_for_element(StellarBurgersLoginLocators.TITLE_FORM).is_displayed()

    @allure.step("Проверка, что пользователь находится на странице личного кабинета")
    def is_at_personal_area(self):
        """Проверяет, что пользователь находится на странице личного кабинета"""
        return self.driver.current_url == URL.PERSONAL_AREA.value

    @allure.step("Проверка, что кнопка выхода отображается")
    def is_exit_button_displayed(self):
        """Проверяет, что кнопка выхода отображается на странице личного кабинета"""
        return self.wait_for_element(StellarBurgersPersonalArea.BUTTON_EXIT).is_displayed()

    @allure.step("Проверка успешного выхода из личного кабинета")
    def is_logged_out(self):
        """Проверяет, что пользователь вышел и находится на странице логина"""
        return self.wait_for_element(StellarBurgersLoginLocators.TITLE_FORM).is_displayed()