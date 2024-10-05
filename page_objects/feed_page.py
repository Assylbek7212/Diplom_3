import allure
from base_page import BasePage
from locators.feed_locators import FeedPageLocators
from data.urls import FEED_URL


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FeedPageLocators  

    @allure.step("Открытие страницы с лентой заказов")
    def open_feed(self):
        """Переход на страницу ленты заказов"""
        self.navigate(FEED_URL, self.locators.FEED_ORDERS)

    @allure.step("Получение списка заказов из ленты")
    def get_feed_orders(self):
        """Получение всех заказов на странице ленты"""
        orders = self.find_elements(self.locators.FEED_ORDERS)
        return [order.text for order in orders]
