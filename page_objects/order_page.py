import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.place_order_button = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        self.order_confirmation = (By.XPATH, "//h1[contains(text(), 'Ваш заказ начали готовить')]")
        self.total_orders_counter = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::span")
        self.today_orders_counter = (By.XPATH, "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::span")
        self.orders_page = (By.XPATH, "//*[contains(text(), 'Лента заказов')]")
        self.order_details_popup = (By.XPATH, "//div[contains(@class, 'modal')]//h2[contains(text(), 'Детали заказа')]")
        self.order_number_in_progress = (By.XPATH, "//p[contains(text(), '№')]")

    @allure.step("Оформление заказа")
    def place_order(self):
        """Клик по кнопке 'Оформить заказ'"""
        self.action_click(self.place_order_button, self.order_confirmation)

    @allure.step("Проверка, что заказ был успешно оформлен")
    def is_order_placed(self):
        """Проверка отображения подтверждения оформления заказа"""
        return self.wait_for_element(self.order_confirmation).is_displayed()

    @allure.step("Открытие страницы 'Лента заказов'")
    def open_orders_page(self):
        """Переход на страницу 'Лента заказов'"""
        self.action_click(self.orders_page, self.order_number_in_progress)

    @allure.step("Клик по номеру заказа")
    def click_order(self):
        """Клик по номеру заказа в списке заказов"""
        self.action_click(self.order_number_in_progress, self.order_details_popup)

    @allure.step("Проверка отображения модального окна с деталями заказа")
    def is_order_details_popup_displayed(self):
        """Проверка отображения всплывающего окна с деталями заказа"""
        return self.wait_for_element(self.order_details_popup).is_displayed()

    @allure.step("Получение общего количества заказов за всё время")
    def get_total_orders_count(self):
        """Получение количества выполненных заказов за всё время"""
        total_orders_element = self.wait_for_element(self.total_orders_counter)
        return int(total_orders_element.text)

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_today_orders_count(self):
        """Получение количества заказов, выполненных за сегодня"""
        today_orders_element = self.wait_for_element(self.today_orders_counter)
        return int(today_orders_element.text)

    @allure.step("Получение ID последнего оформленного заказа")
    def get_order_id(self):
        """Получение идентификатора последнего оформленного заказа"""
        order_confirmation_text = self.wait_for_element(self.order_confirmation).text
        return order_confirmation_text.split('#')[-1].strip()
