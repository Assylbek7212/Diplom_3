from selenium.webdriver.common.by import By


class InProgressPage:
    PROGRESS_ORDERS = (By.XPATH, "//div[contains(@class, 'status-in-progress')]//p[contains(text(), '№')]")
