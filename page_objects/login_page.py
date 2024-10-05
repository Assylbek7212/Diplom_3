# page_objects/login_page.py
import allure
from page_objects.base_page import BasePage
from locators.login_locators import StellarBurgersLoginLocators
from config import URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        """Переход на страницу логина"""
        self.navigate(URL.LOGIN.value, StellarBurgersLoginLocators.TITLE_FORM)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        """Ввод email в форму логина"""
        self.enter_text(StellarBurgersLoginLocators.EMAIL, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """Ввод пароля в форму логина"""
        self.enter_text(StellarBurgersLoginLocators.PASSWORD, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login(self):
        """Клик по кнопке 'Войти' для авторизации"""
        self.action_click(StellarBurgersLoginLocators.BUTTON_LOGIN, StellarBurgersLoginLocators.CHECKOUT_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password(self):
        """Клик по ссылке 'Забыли пароль?' для перехода на страницу восстановления пароля"""
        self.action_click(StellarBurgersLoginLocators.LINK_FORGOT_PASSWORD)

    @allure.step("Авторизация с email: {email}")
    def login(self, email, password):
        """Полная процедура авторизации пользователя"""
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
