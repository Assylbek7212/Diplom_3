import allure

from page_objects.header import Header
from page_objects.home_page import HomePage
from page_objects.personal_area_page import PersonalArea
from locators.personal_area_locators import StellarBurgersPersonalArea
from locators.login_locators import StellarBurgersLoginLocators
from config import URL


class TestForgotPassword:
    @allure.title('Проверка перехода на страницу личного кабинета из авторизованной зоны')
    def test_redirect_click_personal_area_user_authorized(self, web_driver, login):
        header = Header(web_driver)
        header.click_link_personal_area()
        url = web_driver.current_url
        assert url == URL.PERSONAL_AREA.value
        assert web_driver.find_element(*StellarBurgersPersonalArea.BUTTON_EXIT).is_displayed()

    @allure.title('Проверка перехода на страницу личного кабинета из неавторизованной зоны')
    def test_redirect_click_personal_area_user_not_authorized(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.open_home_page()
        header = Header(web_driver)
        header.click_link_personal_area()
        url = web_driver.current_url
        assert url == URL.LOGIN.value
        assert web_driver.find_element(*StellarBurgersLoginLocators.TITLE_FORM).is_displayed()

    @allure.title('Проверка разлогина')
    def test_redirect_click_personal_area_user_authorized(self, web_driver, login):
        header = Header(web_driver)
        personal_area = PersonalArea(web_driver)
        header.click_link_personal_area()
        personal_area.click_button_exit()
        url = web_driver.current_url
        assert url == URL.LOGIN.value
        assert web_driver.find_element(*StellarBurgersLoginLocators.TITLE_FORM).is_displayed()



