# tests/test_personal_area.py
import allure
import pytest
from page_objects.header import Header
from page_objects.personal_area_page import PersonalArea
from page_objects.profile_page import ProfilePage
from page_objects.login_page import LoginPage
from config import URL


@pytest.mark.usefixtures("login")  # Используем фикстуру login, чтобы убедиться, что пользователь авторизован
class TestPersonalArea:

    @allure.title('Проверка перехода на страницу личного кабинета для авторизованного пользователя')
    def test_redirect_to_personal_area_authorized_user(self, web_driver):
        """Проверка перехода на страницу личного кабинета для авторизованного пользователя"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)

        # Клик по ссылке личного кабинета
        header.go_to_personal_area()

        # Проверка, что отображается страница личного кабинета
        assert personal_area.is_at_personal_area(), "Пользователь не перешел в личный кабинет"

        # Проверка, что отображается кнопка выхода
        assert personal_area.is_exit_button_displayed(), "Кнопка выхода не отображается в личном кабинете"

    @allure.title('Проверка перехода на страницу логина для неавторизованного пользователя')
    def test_redirect_to_login_page_for_unauthorized_user(self, web_driver):
        """Проверка перехода на страницу логина для неавторизованного пользователя"""
        home_page = LoginPage(web_driver)
        header = Header(web_driver)

        # Переход на главную страницу
        home_page.open_login_page()

        # Клик по ссылке личного кабинета
        header.go_to_personal_area()

        # Проверка, что пользователь был перенаправлен на страницу логина
        assert home_page.is_at_url(URL.LOGIN.value), "Пользователь не был перенаправлен на страницу логина"

        # Проверка, что форма логина отображается
        assert home_page.wait_for_element(LoginPage.TITLE_FORM).is_displayed(), "Форма логина не отображается"

    @allure.title('Проверка выхода из личного кабинета для авторизованного пользователя')
    def test_logout_from_personal_area_authorized_user(self, web_driver):
        """Проверка выхода из личного кабинета для авторизованного пользователя"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)

        # Переход на страницу личного кабинета
        header.go_to_personal_area()

        # Клик по кнопке выхода
        personal_area.click_button_exit()

        # Проверка, что пользователь был успешно разлогинен и перенаправлен на страницу логина
        assert personal_area.is_logged_out(), "Пользователь не вышел из личного кабинета и не был перенаправлен на страницу логина"

    @allure.title('Проверка изменения информации в профиле пользователя')
    def test_change_user_profile_info(self, web_driver):
        """Проверка изменения информации в профиле пользователя"""
        profile_page = ProfilePage(web_driver)

        # Переход на страницу профиля
        profile_page.open_user_orders()

        # Переход на вкладку "Профиль"
        profile_page.go_to_profile_tab()

        # Изменение имени пользователя (допустим, добавление '_test')
        new_name = "TestUser"
        profile_page.enter_name(new_name)

        # Нажатие кнопки "Сохранить"
        profile_page.click_save_button()

        # Проверка, что имя успешно изменено
        assert profile_page.get_name() == new_name, "Имя пользователя не было успешно изменено"

    @allure.title('Проверка, что пользователь не может зайти в личный кабинет без авторизации')
    def test_access_personal_area_without_login(self, web_driver):
        """Проверка недоступности личного кабинета без авторизации"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)

        # Переход на главную страницу и попытка перехода в личный кабинет
        header.go_to_personal_area()

        # Проверка, что пользователь был перенаправлен на страницу логина
        assert personal_area.is_at_url(URL.LOGIN.value), "Неавторизованный пользователь смог перейти в личный кабинет"
