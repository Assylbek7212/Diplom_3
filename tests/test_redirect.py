import allure
import pytest
from page_objects.header import Header
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage
from page_objects.login_page import LoginPage
from config import DOMEN, URL


@pytest.mark.usefixtures("login")
class TestRedirect:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_on_constructor(self, web_driver):
        """Проверка перехода на страницу конструктора по клику на кнопку в шапке"""
        header = Header(web_driver)
        home_page = HomePage(web_driver)

        header.go_to_constructor()

        home_page.wait_for_element(home_page.locators.DIV_BUNS)

        assert home_page.is_at_url(DOMEN), f"Ожидался URL: {DOMEN}, но получен: {home_page.get_current_url()}"

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_on_order_feed(self, web_driver):
        """Проверка перехода на страницу ленты заказов по клику на кнопку в шапке"""
        header = Header(web_driver)
        order_page = OrderPage(web_driver)

        header.go_to_order_feed()

        order_page.wait_for_element(order_page.locators.ORDERS_PAGE)

        assert order_page.is_at_order_feed(), f"Ожидался URL: {URL.FEED.value}, но получен: {order_page.get_current_url()}"

    @allure.title('Переход по клику на логотип Stellar Burgers')
    def test_click_on_logo_redirects_to_home(self, web_driver):
        """Проверка перехода на главную страницу по клику на логотип"""
        header = Header(web_driver)
        home_page = HomePage(web_driver)

        header.go_to_order_feed()
        header.click_logo()

        home_page.wait_for_element(home_page.locators.LOGIN_BUTTON)

        assert home_page.is_at_url(DOMEN), f"Ожидался URL: {DOMEN}, но получен: {home_page.get_current_url()}"

    @allure.title('Переход на страницу логина при доступе к ленте заказов без авторизации')
    def test_redirect_to_login_when_unauthorized_user_access_feed(self, web_driver):
        """Проверка перехода на страницу логина при попытке неавторизованного пользователя попасть в ленту заказов"""
        login_page = LoginPage(web_driver)
        header = Header(web_driver)

        login_page.open_login_page()

        header.go_to_order_feed()

        assert login_page.is_at_url(URL.LOGIN.value), "Пользователь не был перенаправлен на страницу логина"
