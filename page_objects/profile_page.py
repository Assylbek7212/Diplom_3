import allure
from page_objects.base_page import BasePage
from locators.profile_page_locators import StellarBurgersProfilePageLocators
from data.urls import PROFILE_ORDERS_URL


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StellarBurgersProfilePageLocators

    @allure.step("Открытие страницы заказов пользователя")
    def open_user_orders(self):
        """Переход на страницу заказов пользователя в личном кабинете"""
        self.navigate(PROFILE_ORDERS_URL, self.locators.USER_ORDERS)

    @allure.step("Получение списка заказов пользователя")
    def get_user_orders(self):
        """Возвращает список заказов пользователя на странице личного кабинета"""
        orders = self.find_elements(self.locators.USER_ORDERS)
        return [order.text for order in orders]

    @allure.step("Клик по вкладке 'Профиль'")
    def go_to_profile_tab(self):
        """Переход на вкладку 'Профиль' в личном кабинете"""
        self.action_click(self.locators.PROFILE_TAB)

    @allure.step("Выход из аккаунта")
    def logout(self):
        """Клик по кнопке выхода из аккаунта"""
        self.action_click(self.locators.LOGOUT_BUTTON)
