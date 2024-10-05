import allure
from page_objects.base_page import BasePage
from locators.personal_area_locators import StellarBurgersPersonalArea
from locators.login_locators import StellarBurgersLoginLocators
from config import URL


class PersonalArea(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StellarBurgersPersonalArea

    @allure.step("Клик по кнопке выхода из личного кабинета")
    def click_button_exit(self):
        """Клик по кнопке 'Выход' на странице личного кабинета"""
        self.action_click(self.locators.BUTTON_EXIT, StellarBurgersLoginLocators.TITLE_FORM)

    @allure.step("Проверка, что произошел успешный выход на страницу логина")
    def is_logged_out(self):
        """Проверяет, что после выхода отображается форма логина"""
        return self.wait_for_element(StellarBurgersLoginLocators.TITLE_FORM).is_displayed()

    @allure.step("Проверка нахождения в личном кабинете")
    def is_at_personal_area(self):
        """Проверка, что пользователь находится на странице личного кабинета"""
        return self.is_element_visible(self.locators.TITLE_PERSONAL_AREA)

    @allure.step("Проверка наличия кнопки 'Выход' в личном кабинете")
    def is_exit_button_displayed(self):
        """Проверка отображения кнопки 'Выход'"""
        return self.is_element_visible(self.locators.BUTTON_EXIT)

    @allure.step("Клик по кнопке 'Выход'")
    def click_button_exit(self):
        """Клик по кнопке 'Выход' в личном кабинете"""
        self.action_click(self.locators.BUTTON_EXIT)

    @allure.step("Проверка перехода на страницу логина")
    def is_logged_out(self):
        """Проверка, что пользователь разлогинился"""
        return self.is_at_url(URL.LOGIN.value)