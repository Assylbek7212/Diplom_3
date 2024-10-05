from selenium.webdriver.common.by import By

class StellarBurgersProfilePageLocators:
    USER_ORDERS = (By.XPATH, "//div[contains(@class, 'profile__order')]")
    PROFILE_TAB = (By.XPATH, "//a[contains(@href, '/profile')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
