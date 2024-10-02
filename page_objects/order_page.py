from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.place_order_button = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        self.order_confirmation = (By.XPATH, "//h1[contains(text(), 'Ваш заказ начали готовить')]")
        self.total_orders_counter = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::span")
        self.today_orders_counter = (By.XPATH, "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::span")
        self.orders_page = (By.XPATH, "//*[contains(text(), 'Лента заказов')]")
        self.order_details_popup = (By.XPATH, "//div[contains(@class, 'modal')]//h2[contains(text(), 'Детали заказа')]")
        self.order_number_in_progress = (By.XPATH, "//p[contains(text(), '№')]")

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()

    def is_order_placed(self):
        return self.driver.find_element(*self.order_confirmation).is_displayed()

    def open_orders_page(self):
        self.driver.find_element(*self.orders_page).click()

    def click_order(self):
        self.driver.find_element(*self.order_number_in_progress).click()

    def is_order_details_popup_displayed(self):
        return self.driver.find_element(*self.order_details_popup).is_displayed()

    def get_total_orders_count(self):
        return int(self.driver.find_element(*self.total_orders_counter).text)

    def get_today_orders_count(self):
        return int(self.driver.find_element(*self.today_orders_counter).text)

    def get_order_id(self):
        return self.driver.find_element(*self.order_confirmation).text.split('#')[-1]
