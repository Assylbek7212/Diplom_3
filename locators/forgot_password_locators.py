from selenium.webdriver.common.by import By

class StellarBurgersForgotPasswordLocators:
    EMAIL = (By.XPATH, "//input[@name='name']")
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//button[text()='Восстановить']")
