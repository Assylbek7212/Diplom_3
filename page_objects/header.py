import allure
from page_objects.base_page import BasePage
from locators.header_locators import StellarBurgersHeader

class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StellarBurgersHeader

    @allure.step("Клик по элементу '{element_name}' в шапке сайта")
    def click_header_button(self, locator, element_name="Элемент"):
        """Клик по указанному элементу шапки сайта и ожидание загрузки логотипа"""
        self.action_click(locator, self.locators.LINK_LOGO)

    @allure.step("Переход в раздел 'Конструктор'")
    def go_to_constructor(self):
        """Клик по кнопке 'Конструктор' и ожидание появления элемента"""
        self.action_click(self.locators.LINK_CONSTRUCTOR, self.locators.LINK_LOGO)

    @allure.step("Переход в 'Лента заказов'")
    def go_to_order_feed(self):
        """Клик по кнопке 'Лента заказов' и ожидание появления элемента"""
        self.action_click(self.locators.LINK_ORDER_FEED)

    @allure.step("Переход в раздел 'Личный кабинет'")
    def go_to_personal_area(self):
        """Клик по кнопке 'Личный кабинет' и ожидание загрузки страницы"""
        self.action_click(self.locators.LINK_PERSONAL_AREA, self.locators.LINK_LOGO)

    @allure.step("Проверка нахождения на главной странице")
    def is_at_main_page(self):
        """Проверка, что пользователь находится на главной странице"""
        return self.is_element_visible(self.locators.LINK_CONSTRUCTOR)

    @allure.step("Проверка, что элемент присутствует")
    def is_element_visible(self, locator, timeout=10):
        """Проверка, что элемент присутствует на странице"""
        return self.wait_for_element(locator, timeout).is_displayed()

    @allure.step("Клик по логотипу для перехода на главную страницу")
    def click_logo(self):
        """Клик по логотипу Stellar Burgers в шапке сайта"""
        self.action_click(self.locators.LINK_LOGO)
