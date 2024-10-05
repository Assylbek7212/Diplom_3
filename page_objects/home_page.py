import allure
from page_objects.base_page import BasePage
from locators.home_page_locators import StellarBurgersHomePageLocators
from config import DOMEN


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие главной страницы сайта")
    def open_home_page(self):
        """Переход на главную страницу сайта"""
        self.navigate(DOMEN, StellarBurgersHomePageLocators.LOGIN_BUTTON)

    @allure.step("Проверка, что кнопка 'Войти в аккаунт' отображается")
    def is_login_button_displayed(self):
        """Проверка отображения кнопки 'Войти в аккаунт'"""
        return self.wait_for_element(StellarBurgersHomePageLocators.LOGIN_BUTTON).is_displayed()

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        """Клик по кнопке 'Войти в аккаунт'"""
        self.action_click(StellarBurgersHomePageLocators.LOGIN_BUTTON)

    @allure.step("Клик по флуоресцентной булочке")
    def click_fluorescent_bun(self):
        """Клик по элементу флуоресцентной булочки"""
        self.action_click(StellarBurgersHomePageLocators.BUN_FLUORESCENT)

    @allure.step("Получение имени флуоресцентной булочки")
    def get_fluorescent_bun_name(self):
        """Получение текста названия флуоресцентной булочки"""
        return self.wait_for_element(StellarBurgersHomePageLocators.NAME_BUN_FLUORESCENT).text

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_checkout_button(self):
        """Клик по кнопке 'Оформить заказ' на главной странице"""
        self.action_click(StellarBurgersHomePageLocators.CHECKOUT_BUTTON)
