import allure
from page_objects.base_page import BasePage
from ..data.urls import FEED_URL
from locators.in_progress_locators import InProgressPage

class InProgressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы с заказами в процессе выполнения")
    def open_in_progress_orders(self):
        """Переход на страницу с заказами в процессе выполнения"""
        self.go_to(FEED_URL)

    @allure.step("Получение списка ID заказов в процессе выполнения")
    def get_in_progress_order_ids(self):
        """Получение списка ID всех заказов в статусе 'В процессе выполнения'"""
        orders = self.find_elements(InProgressPage.PROGRESS_ORDERS)
        return [order.text.split('№')[-1].strip() for order in orders]
