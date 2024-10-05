import allure
import pytest
from page_objects.header import Header
from page_objects.personal_area_page import PersonalArea
from page_objects.profile_page import ProfilePage
from page_objects.login_page import LoginPage
from config import URL
from locators.login_locators import StellarBurgersLoginLocators



@pytest.mark.usefixtures("login")
class TestPersonalArea:

    @allure.title('Проверка перехода на страницу личного кабинета для авторизованного пользователя')
    def test_redirect_to_personal_area_authorized_user(self, web_driver):
        """Проверка перехода на страницу личного кабинета для авторизованного пользователя"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)

        header.go_to_personal_area()

        assert personal_area.is_at_personal_area(), "Пользователь не перешел в личный кабинет"

        assert personal_area.is_exit_button_displayed(), "Кнопка выхода не отображается в личном кабинете"

    @allure.title('Проверка перехода на страницу логина для неавторизованного пользователя')
    def test_redirect_to_login_page_for_unauthorized_user(self, web_driver):
        """Проверка перехода на страницу логина для неавторизованного пользователя"""
        home_page = LoginPage(web_driver)
        header = Header(web_driver)

        home_page.open_login_page()

        header.go_to_personal_area()

        assert home_page.is_at_url(URL.LOGIN.value), "Пользователь не был перенаправлен на страницу логина"

        assert home_page.wait_for_element(StellarBurgersLoginLocators.TITLE_FORM).is_displayed(), "Форма логина не отображается"

    @allure.title('Проверка выхода из личного кабинета для авторизованного пользователя')
    def test_logout_from_personal_area_authorized_user(self, web_driver):
        """Проверка выхода из личного кабинета для авторизованного пользователя"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)

        header.go_to_personal_area()

        personal_area.click_button_exit()


    @allure.title('Проверка изменения информации в профиле пользователя')
    def test_change_user_profile_info(self, web_driver):
        """Проверка изменения информации в профиле пользователя"""
        profile_page = ProfilePage(web_driver)

        profile_page.open_user_orders()

        profile_page.go_to_profile_tab()

        new_name = "TestUser"
        profile_page.enter_name(new_name)

        profile_page.click_save_button()

        assert profile_page.get_name() == new_name, "Имя пользователя не было успешно изменено"

    @allure.title('Проверка, что пользователь не может зайти в личный кабинет без авторизации')
    def test_access_personal_area_without_login(self, web_driver):
        """Проверка недоступности личного кабинета без авторизации"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)

        header.go_to_personal_area()

        assert personal_area.is_at_url(URL.LOGIN.value), "Неавторизованный пользователь смог перейти в личный кабинет"
