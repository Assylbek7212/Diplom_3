import allure
from page_objects.header import Header
from page_objects.home_page import HomePage
from page_objects.personal_area_page import PersonalArea
from locators.personal_area_locators import StellarBurgersPersonalArea
from locators.login_locators import StellarBurgersLoginLocators
from config import URL


class TestForgotPassword:
    @allure.title('Проверка перехода на страницу личного кабинета из авторизованной зоны')
    def test_redirect_to_personal_area_authorized_user(self, web_driver, login):
        """Проверка перехода в личный кабинет для авторизованного пользователя"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)
        header.click_link_personal_area()
        assert personal_area.is_at_personal_area(), "Пользователь не перешел в личный кабинет"
        assert personal_area.is_exit_button_displayed(), "Кнопка выхода не отображается"

    @allure.title('Проверка перехода на страницу логина из неавторизованной зоны')
    def test_redirect_to_login_page_for_unauthorized_user(self, web_driver):
        """Проверка перехода на страницу логина при неавторизованном пользователе"""
        home_page = HomePage(web_driver)
        header = Header(web_driver)

        home_page.open_home_page()
        header.click_link_personal_area()
        assert home_page.is_at_login_page(), "Пользователь не был перенаправлен на страницу логина"
        assert home_page.is_login_form_displayed(), "Форма логина не отображается"

    @allure.title('Проверка выхода из личного кабинета для авторизованного пользователя')
    def test_logout_from_personal_area_authorized_user(self, web_driver, login):
        """Проверка разлогина и перехода на страницу логина"""
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)
        header.click_link_personal_area()
        personal_area.click_button_exit()
        assert personal_area.is_logged_out(), "Пользователь не вышел из личного кабинета"
