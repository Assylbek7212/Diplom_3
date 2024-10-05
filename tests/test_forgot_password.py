import allure
import pytest
from page_objects.login_page import LoginPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.reset_password_page import ResetPasswordPage
from config import URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForgotPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_page_opening_forgot_password(self, web_driver):
        """Проверка, что пользователь может перейти на страницу восстановления пароля из логина"""
        login_page = LoginPage(web_driver)
        login_page.open_login_page()

        login_page.go_to_forgot_password()

        WebDriverWait(web_driver, 10).until(EC.url_to_be(URL.FORGOT_PASSWORD.value))

        assert login_page.is_at_url(URL.FORGOT_PASSWORD.value), "Пользователь не был перенаправлен на страницу восстановления пароля"

    @allure.title('Проверка ввода почты на странице восстановления пароля и клика по кнопке «Восстановить»')
    def test_page_enter_email_and_redirect_reset_password(self, web_driver):
        """Проверка ввода email и перехода на страницу сброса пароля"""
        forgot_password = ForgotPasswordPage(web_driver)
        forgot_password.open_forgot_password_page()

        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()

        WebDriverWait(web_driver, 10).until(EC.url_to_be(URL.RESET_PASSWORD.value))

        url = web_driver.current_url
        assert url == URL.RESET_PASSWORD.value, f"Ожидался URL: {URL.RESET_PASSWORD.value}, но получен: {url}"

    @allure.title('Проверка отображения скрытого пароля')
    def test_whether_hidden_password(self, web_driver):
        """Проверка отображения скрытого пароля при вводе"""
        forgot_password = ForgotPasswordPage(web_driver)
        reset_password = ResetPasswordPage(web_driver)

        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()

        reset_password.enter_password("SecretPassword")
        assert reset_password.get_attribute_password() == "password", "Пароль не скрыт"

    @allure.title('Проверка отображения видимого пароля')
    def test_whether_visible_password(self, web_driver):
        """Проверка видимости пароля после клика по кнопке 'Показать/Скрыть'"""
        forgot_password = ForgotPasswordPage(web_driver)
        reset_password = ResetPasswordPage(web_driver)

        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()

        reset_password.enter_password("SecretPassword")
        reset_password.click_button_action_password()

        assert reset_password.get_attribute_password() == "text", "Пароль не отображается в виде текста"
