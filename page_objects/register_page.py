import allure
from page_objects.base_page import BasePage
from locators.register_locators import StellarBurgersRegister
from config import URL


class RegisterPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.locators = StellarBurgersRegister

    @allure.step("Открытие страницы регистрации")
    def open_register_page(self):
        """Переход на страницу регистрации"""
        self.navigate(URL.REGISTER.value, self.locators.EMAIL)

    @allure.step("Ввод имени: {name}")
    def enter_name(self, name):
        """Ввод имени в поле регистрации"""
        self.enter_text(self.locators.NAME, name)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        """Ввод email в поле регистрации"""
        self.enter_text(self.locators.EMAIL, email)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        """Ввод пароля в поле регистрации"""
        self.enter_text(self.locators.PASSWORD, password)

    @allure.step("Клик по кнопке регистрации")
    def click_register(self):
        """Клик по кнопке 'Зарегистрироваться'"""
        self.action_click(self.locators.SUBMIT_BUTTON, self.locators.TITLE_FORM)

    @allure.step("Регистрация нового пользователя с именем {name}, email {email}")
    def signup(self, name, email, password):
        """Полный процесс регистрации нового пользователя"""
        self.open_register_page()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register()

    @allure.step("Проверка, что регистрация прошла успешно и отображается страница логина")
    def is_registration_successful(self):
        """Проверка успешного завершения регистрации по наличию формы логина"""
        return self.wait_for_element(self.locators.TITLE_FORM).is_displayed()
