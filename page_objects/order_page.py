import allure
from page_objects.base_page import BasePage
from locators.order_feed_page_locators import StellarBurgersOrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StellarBurgersOrderPageLocators

    @allure.step("Оформление заказа")
    def place_order(self):
        """Клик по кнопке 'Оформить заказ'"""
        self.action_click(self.locators.PLACE_ORDER_BUTTON, self.locators.ORDER_CONFIRMATION)

    @allure.step("Проверка, что заказ был успешно оформлен")
    def is_order_placed(self):
        """Проверка отображения подтверждения оформления заказа"""
        return self.wait_for_element(self.locators.ORDER_CONFIRMATION).is_displayed()

    @allure.step("Открытие страницы 'Лента заказов'")
    def open_orders_page(self):
        """Переход на страницу 'Лента заказов'"""
        self.action_click(self.locators.ORDERS_PAGE, self.locators.ORDER_NUMBER_IN_PROGRESS)

    @allure.step("Клик по номеру заказа")
    def click_order(self):
        """Клик по номеру заказа в списке заказов"""
        self.action_click(self.locators.ORDER_NUMBER_IN_PROGRESS, self.locators.ORDER_DETAILS_POPUP)

    @allure.step("Проверка отображения модального окна с деталями заказа")
    def is_order_details_popup_displayed(self):
        """Проверка отображения всплывающего окна с деталями заказа"""
        return self.wait_for_element(self.locators.ORDER_DETAILS_POPUP).is_displayed()

    @allure.step("Получение общего количества заказов за всё время")
    def get_total_orders_count(self):
        """Получение количества выполненных заказов за всё время"""
        total_orders_element = self.wait_for_element(self.locators.TOTAL_ORDERS_COUNTER)
        return int(total_orders_element.text)

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_today_orders_count(self):
        """Получение количества заказов, выполненных за сегодня"""
        today_orders_element = self.wait_for_element(self.locators.TODAY_ORDERS_COUNTER)
        return int(today_orders_element.text)

    @allure.step("Получение ID последнего оформленного заказа")
    def get_order_id(self):
        """Получение идентификатора последнего оформленного заказа"""
        order_confirmation_text = self.wait_for_element(self.locators.ORDER_CONFIRMATION).text
        return order_confirmation_text.split('#')[-1].strip()
