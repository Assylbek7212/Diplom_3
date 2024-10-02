from selenium.webdriver.common.by import By


class StellarBurgersForgotPasswordLocators:
    EMAIL = (By.XPATH, "//input[@name = 'name']")  # поле ввода email
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//button[text()= 'Восстановить']")  # кнопка восстановления пароля
