from selenium.webdriver.common.by import By

class InProgressPage:
    def __init__(self, driver):
        self.driver = driver
        self.in_progress_orders = (By.XPATH, "//div[contains(@class, 'status-in-progress')]//p[contains(text(), '№')]")

    def open_in_progress_orders(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    def get_in_progress_order_ids(self):
        return [order.text.split('№')[-1].strip() for order in self.driver.find_elements(*self.in_progress_orders)]
