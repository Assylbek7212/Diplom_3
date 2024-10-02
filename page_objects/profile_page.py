from selenium.webdriver.common.by import By

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.user_orders = (By.XPATH, "//div[contains(@class, 'profile__order')]")

    def open_user_orders(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/profile/orders")

    def get_user_orders(self):
        return [order.text for order in self.driver.find_elements(*self.user_orders)]
