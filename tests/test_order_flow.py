# tests/test_order_flow.py
import allure
import pytest
from page_objects.ingredient_page import IngredientPage
from page_objects.order_page import OrderPage
from page_objects.profile_page import ProfilePage
from page_objects.feed_page import FeedPage
from page_objects.in_progress_page import InProgressPage


@pytest.mark.usefixtures("login")  # Используем фикстуру login, чтобы убедиться, что пользователь авторизован
class TestOrderFlow:

    @allure.title('Увеличение счётчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases_after_addition(self, web_driver):
        """Проверка увеличения счётчика ингредиента после добавления в заказ"""
        ingredient_page = IngredientPage(web_driver)

        # Добавляем ингредиент в заказ
        ingredient_page.add_ingredient()

        # Проверяем, что счетчик увеличился
        assert ingredient_page.is_counter_increased(), "Счётчик ингредиента не увеличился после добавления"

    @allure.title('Возможность залогиненного пользователя оформить заказ')
    def test_logged_in_user_can_place_order(self, web_driver):
        """Проверка оформления заказа авторизованным пользователем"""
        order_page = OrderPage(web_driver)

        # Переход на страницу оформления заказа и выполнение заказа
        order_page.open_orders_page()
        order_page.place_order()

        # Проверка, что заказ был успешно оформлен
        assert order_page.is_order_placed(), "Заказ не был успешно оформлен"

    @allure.title('Открытие всплывающего окна с деталями заказа')
    def test_order_details_popup_opens_on_click(self, web_driver):
        """Проверка открытия всплывающего окна с деталями заказа"""
        order_page = OrderPage(web_driver)

        # Переход на страницу заказов и открытие деталей заказа
        order_page.open_orders_page()
        order_page.click_order()

        # Проверка, что модальное окно открылось
        assert order_page.is_order_details_popup_displayed(), "Модальное окно с деталями заказа не открылось"

    @allure.title('Заказы пользователя отображаются в «Ленте заказов»')
    def test_user_orders_displayed_in_order_feed(self, web_driver):
        """Проверка отображения заказов пользователя в «Ленте заказов»"""
        profile_page = ProfilePage(web_driver)
        feed_page = FeedPage(web_driver)

        # Переход на страницу личного кабинета и получение списка заказов пользователя
        profile_page.open_user_orders()
        user_orders = profile_page.get_user_orders()

        # Переход на страницу ленты заказов и получение списка заказов из ленты
        feed_page.open_feed()
        feed_orders = feed_page.get_feed_orders()

        # Сравнение списка заказов пользователя и ленты заказов
        for order in user_orders:
            assert order in feed_orders, f"Заказ {order} не отображается в ленте заказов"

    @allure.title('Увеличение счётчика «Выполнено за всё время» при создании нового заказа')
    def test_total_orders_counter_increases(self, web_driver):
        """Проверка увеличения счётчика выполненных заказов за всё время"""
        order_page = OrderPage(web_driver)

        # Переход на страницу заказов и получение текущего значения счетчика
        order_page.open_orders_page()
        initial_count = order_page.get_total_orders_count()

        # Оформление нового заказа
        order_page.place_order()

        # Получение нового значения счетчика
        new_count = order_page.get_total_orders_count()

        # Проверка увеличения счетчика
        assert new_count == initial_count + 1, "Счётчик выполненных заказов за всё время не увеличился"

    @allure.title('Увеличение счётчика «Выполнено за сегодня» при создании нового заказа')
    def test_today_orders_counter_increases(self, web_driver):
        """Проверка увеличения счётчика выполненных заказов за сегодня"""
        order_page = OrderPage(web_driver)

        # Переход на страницу заказов и получение текущего значения счетчика
        order_page.open_orders_page()
        initial_count = order_page.get_today_orders_count()

        # Оформление нового заказа
        order_page.place_order()

        # Получение нового значения счетчика
        new_count = order_page.get_today_orders_count()

        # Проверка увеличения счетчика
        assert new_count == initial_count + 1, "Счётчик выполненных заказов за сегодня не увеличился"

    @allure.title('Появление номера заказа в разделе «В работе» после оформления')
    def test_order_number_appears_in_in_progress_section(self, web_driver):
        """Проверка отображения номера заказа в разделе «В работе» после оформления"""
        order_page = OrderPage(web_driver)

        # Переход на страницу заказов и оформление нового заказа
        order_page.open_orders_page()
        order_page.place_order()

        # Получение ID оформленного заказа
        order_id = order_page.get_order_id()

        # Переход на страницу заказов в процессе выполнения
        in_progress_page = InProgressPage(web_driver)
        in_progress_page.open_in_progress_orders()

        # Проверка, что заказ отображается в разделе "В работе"
        assert order_id in in_progress_page.get_in_progress_order_ids(), f"Заказ {order_id} не отображается в разделе «В работе»"
