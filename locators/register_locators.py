from selenium.webdriver.common.by import By


class StellarBurgersRegister:
    NAME = (By.XPATH, "//label[text() = 'Имя']/following::input[1]")  # поле ввода имени
    EMAIL = (By.XPATH, "//label[text() = 'Email']/following::input[1]")  # поле ввода email
    PASSWORD = (By.XPATH, "//input[@name = 'Пароль']")  # поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[text()= 'Зарегистрироваться']")  # кнопка 'Зарегистрироваться'
