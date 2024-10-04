import allure
from locators.feed_locators import FeedPageLocators
from base_page import BasePage
from ..data.urls import FEED_URL

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FeedPageLocators

    @allure.step("Открытие страницы с лентой заказов")
    def open_feed(self):
        """Открытие страницы с лентой заказов"""
        self.go_to(FEED_URL)

    @allure.step("Получение списка заказов из ленты")
    def get_feed_orders(self):
        """Получение всех заказов на странице ленты"""
        orders = self.find_elements(self.locators.FEED_ORDERS)
        return [order.text for order in orders]
