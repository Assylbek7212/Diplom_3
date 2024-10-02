from selenium.webdriver.common.by import By

class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.feed_orders = (By.XPATH, "//div[contains(@class, 'feed__order')]")

    def open_feed(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    def get_feed_orders(self):
        return [order.text for order in self.driver.find_elements(*self.feed_orders)]
