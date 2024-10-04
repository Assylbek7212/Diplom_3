import allure
from page_objects.base_page import BasePage
from locators.header_locators import StellarBurgersHeader


class Header(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_link_personal_area(self):
        """Клик по кнопке 'Личный кабинет' в шапке сайта и ожидание загрузки логотипа"""
        self.action_click(StellarBurgersHeader.PERSONAL_AREA_BUTTON,
                          StellarBurgersHeader.LINK_LOGO)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_link_constructor(self):
        """Клик по кнопке 'Конструктор' в шапке сайта и ожидание загрузки логотипа"""
        self.action_click(StellarBurgersHeader.LINK_CONSTRUCTOR,
                          StellarBurgersHeader.LINK_LOGO)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_link_order_feed(self):
        """Клик по кнопке 'Лента заказов' в шапке сайта и ожидание загрузки логотипа"""
        self.action_click(StellarBurgersHeader.LINK_ORDER_FEED,
                          StellarBurgersHeader.LINK_LOGO)
