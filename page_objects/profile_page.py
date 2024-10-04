import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from ..data.urls import PROFILE_ORDERS_URL  # Импортируем URL из модуля urls

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.user_orders = (By.XPATH, "//div[contains(@class, 'profile__order')]")

    @allure.step("Открытие страницы заказов пользователя")
    def open_user_orders(self):
        """Переход на страницу заказов пользователя в личном кабинете"""
        self.go_to(PROFILE_ORDERS_URL)

    @allure.step("Получение списка заказов пользователя")
    def get_user_orders(self):
        """Возвращает список заказов пользователя на странице личного кабинета"""
        orders = self.find_elements(self.user_orders)
        return [order.text for order in orders]
