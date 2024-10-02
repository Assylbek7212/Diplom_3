import allure
import pytest
from page_objects.login_page import LoginPage
from page_objects.ingredient_page import IngredientPage
from page_objects.order_page import OrderPage
from page_objects.profile_page import ProfilePage
from page_objects.feed_page import FeedPage
from page_objects.in_progress_page import InProgressPage
from config import URL

@pytest.mark.usefixtures("setup")
class TestOrderFlow:

    @allure.title('Увеличение счётчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases_after_addition(self, web_driver):
        ingredient_page = IngredientPage(web_driver)
        ingredient_page.add_ingredient()
        assert ingredient_page.is_counter_increased()

    @allure.title('Возможность залогиненного пользователя оформить заказ')
    def test_logged_in_user_can_place_order(self, web_driver, login):
        login_page = LoginPage(web_driver)
        order_page = OrderPage(web_driver)
        login_page.login('username', 'password')
        order_page.place_order()
        assert order_page.is_order_placed()

    @allure.title('Открытие всплывающего окна с деталями заказа')
    def test_order_details_popup_opens_on_click(self, web_driver, login):
        order_page = OrderPage(web_driver)
        order_page.open_orders_page()
        order_page.click_order()
        assert order_page.is_order_details_popup_displayed()

    @allure.title('Заказы пользователя отображаются в «Ленте заказов»')
    def test_user_orders_displayed_in_order_feed(self, web_driver, login):
        profile_page = ProfilePage(web_driver)
        feed_page = FeedPage(web_driver)
        profile_page.open_user_orders()
        user_orders = profile_page.get_user_orders()
        feed_page.open_feed()
        feed_orders = feed_page.get_feed_orders()
        for order in user_orders:
            assert order in feed_orders

    @allure.title('Увеличение счётчика «Выполнено за всё время» при создании нового заказа')
    def test_total_orders_counter_increases(self, web_driver, login):
        order_page = OrderPage(web_driver)
        initial_count = order_page.get_total_orders_count()
        order_page.place_order()
        new_count = order_page.get_total_orders_count()
        assert new_count == initial_count + 1

    @allure.title('Увеличение счётчика «Выполнено за сегодня» при создании нового заказа')
    def test_today_orders_counter_increases(self, web_driver, login):
        order_page = OrderPage(web_driver)
        initial_count = order_page.get_today_orders_count()
        order_page.place_order()
        new_count = order_page.get_today_orders_count()
        assert new_count == initial_count + 1

    @allure.title('Появление номера заказа в разделе «В работе» после оформления')
    def test_order_number_appears_in_in_progress_section(self, web_driver, login):
        order_page = OrderPage(web_driver)
        order_page.place_order()
        order_id = order_page.get_order_id()
        in_progress_page = InProgressPage(web_driver)
        in_progress_page.open_in_progress_orders()
        assert order_id in in_progress_page.get_in_progress_order_ids()
