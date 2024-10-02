from selenium.webdriver.common.by import By


class StellarBurgersResetPasswordLocators:
    PASSWORD = (By.XPATH, "//input[@name = 'Введите новый пароль']")  # поле ввода пароля
    BUTTON_ACTION_PASSWORD = By.XPATH, "//*[contains(@class, 'input__icon-action')]" # кнопка показать/скрыть пароль
