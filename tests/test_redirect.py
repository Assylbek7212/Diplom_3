import allure

from page_objects.header import Header
from locators.home_page_locators import StellarBurgersHomePageLocators
from locators.order_feed_page_locators import StellarBurgersOrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import DOMEN, URL


class TestRedirect:

    @allure.title('переход по клику на «Конструктор»')
    def test_click_on_constructor(self, web_driver):
        header = Header(web_driver)
        header.click_link_personal_area()
        header.click_link_constructor()
        WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
            StellarBurgersHomePageLocators.DIV_BUNS))
        url = web_driver.current_url
        assert url == DOMEN
        assert web_driver.find_element(*StellarBurgersHomePageLocators.DIV_BUNS).is_displayed()

    @allure.title('переход по клику на «Лента заказов»')
    def test_click_on_order_feed(self, web_driver):
        header = Header(web_driver)
        header.click_link_order_feed()
        WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
            StellarBurgersOrderFeedLocators.TITLE_FORM))
        url = web_driver.current_url
        assert url == URL.FEED.value
        assert web_driver.find_element(*StellarBurgersOrderFeedLocators.TITLE_FORM).is_displayed()
