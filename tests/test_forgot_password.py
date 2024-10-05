# tests/test_forgot_password.py
import allure
from page_objects.login_page import LoginPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.reset_password_page import ResetPasswordPage
from config import URL


class TestForgotPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_page_opening_forgot_password(self, web_driver):
        """Проверка, что пользователь может перейти на страницу восстановления пароля из логина"""
        login_page = LoginPage(web_driver)
        login_page.open_login_page()

        # Клик по ссылке "Забыли пароль?"
        login_page.go_to_forgot_password()

        # Проверка текущего URL
        url = web_driver.current_url
        assert url == URL.FORGOT_PASSWORD.value, f"Ожидался URL: {URL.FORGOT_PASSWORD.value}, но получен: {url}"

    @allure.title('Проверка ввода почты на странице восстановления пароля и клика по кнопке «Восстановить»')
    def test_page_enter_email_and_redirect_reset_password(self, web_driver):
        """Проверка ввода email и перехода на страницу сброса пароля"""
        forgot_password = ForgotPasswordPage(web_driver)
        forgot_password.open_forgot_password_page()

        # Ввод email и клик по кнопке "Восстановить"
        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()

        # Проверка текущего URL
        url = web_driver.current_url
        assert url == URL.RESET_PASSWORD.value, f"Ожидался URL: {URL.RESET_PASSWORD.value}, но получен: {url}"

    @allure.title('Проверка отображения скрытого пароля')
    def test_whether_hidden_password(self, web_driver):
        """Проверка отображения скрытого пароля при вводе"""
        forgot_password = ForgotPasswordPage(web_driver)
        reset_password = ResetPasswordPage(web_driver)

        # Переход на страницу сброса пароля и ввод пароля
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()
        reset_password.enter_password()

        # Проверка типа поля (должен быть скрыт)
        assert reset_password.get_attribute_password() == "password", "Пароль отображается открытым"

    @allure.title('Проверка отображения видимого пароля')
    def test_whether_visible_password(self, web_driver):
        """Проверка видимости пароля после клика по кнопке 'Показать/Скрыть'"""
        forgot_password = ForgotPasswordPage(web_driver)
        reset_password = ResetPasswordPage(web_driver)

        # Переход на страницу сброса пароля и ввод пароля
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email("test@example.com")
        forgot_password.click_button_restore_password()
        reset_password.enter_password()

        # Клик по кнопке "Показать пароль"
        reset_password.click_button_action_password()

        # Проверка, что пароль стал видимым
        assert reset_password.get_attribute_password() == "text", "Пароль не отображается открытым"
