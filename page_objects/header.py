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

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def go_to_personal_area(self):
        """Клик по кнопке 'Личный кабинет' в шапке сайта"""
        self.click_header_button(self.locators.PERSONAL_AREA_BUTTON, "Личный кабинет")

    @allure.step("Клик по кнопке 'Конструктор'")
    def go_to_constructor(self):
        """Клик по кнопке 'Конструктор' в шапке сайта"""
        self.click_header_button(self.locators.LINK_CONSTRUCTOR, "Конструктор")

    @allure.step("Клик по кнопке 'Лента заказов'")
    def go_to_order_feed(self):
        """Клик по кнопке 'Лента заказов' в шапке сайта"""
        self.click_header_button(self.locators.LINK_ORDER_FEED, "Лента заказов")

    @allure.step("Клик по логотипу")
    def click_logo(self):
        """Клик по логотипу Stellar Burgers в шапке сайта"""
        self.click_header_button(self.locators.LINK_LOGO, "Логотип")
