from selenium.webdriver.common.by import By


class StellarBurgersLoginLocators:
    TITLE_FORM = (By.XPATH, "//h2[text()='Вход']")  # Название формы авторизации
    EMAIL = (By.XPATH, "//input[@name = 'name']")  # поле ввода email
    PASSWORD = (By.XPATH, "//input[@name = 'Пароль']")  # поле ввода пароля
    BUTTON_LOGIN = (By.XPATH, "//button[text()= 'Войти']")  # кнопка 'Войти'
    LINK_FORGOT_PASSWORD = (By.XPATH, "//*/a[@href='/forgot-password']") # ссылка на страницу восстановления пароля
