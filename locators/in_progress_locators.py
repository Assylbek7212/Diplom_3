from selenium.webdriver.common.by import By

class InProgressPageLocators:
    PROGRESS_ORDERS = (By.XPATH, "//div[contains(@class, 'status-in-progress')]//p[contains(text(), '№')]")
