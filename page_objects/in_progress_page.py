import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from ..data.urls import FEED_URL

class InProgressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Инициализация базового класса
        self.in_progress_orders = (By.XPATH, "//div[contains(@class, 'status-in-progress')]//p[contains(text(), '№')]")

    @allure.step("Открытие страницы с заказами в процессе выполнения")
    def open_in_progress_orders(self):
        """Переход на страницу с заказами в процессе выполнения"""
        self.go_to(FEED_URL)  # Используем метод `go_to` из базового класса

    @allure.step("Получение списка ID заказов в процессе выполнения")
    def get_in_progress_order_ids(self):
        """Получение списка ID всех заказов в статусе 'В процессе выполнения'"""
        orders = self.find_elements(self.in_progress_orders)  # Используем метод `find_elements` из BasePage
        return [order.text.split('№')[-1].strip() for order in orders]
