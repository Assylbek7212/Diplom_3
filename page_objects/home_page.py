import allure
from page_objects.base_page import BasePage
from locators.home_page_locators import StellarBurgersHomePageLocators
from locators.login_locators import StellarBurgersLoginLocators
from config import DOMEN
from config import URL

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка, что пользователь находится на странице логина")
    def is_at_login_page(self):
        """Проверяет, что пользователь находится на странице логина"""
        return self.driver.current_url == URL.LOGIN.value

    @allure.step("Проверка, что форма логина отображается")
    def is_login_form_displayed(self):
        """Проверяет, что форма логина отображается на странице"""
        return self.wait_for_element(StellarBurgersLoginLocators.TITLE_FORM).is_displayed()
    @allure.step("Получение названия флуоресцентной булочки на главной странице")
    def get_fluorescent_bun_name(self):
        """Получение имени флуоресцентной булочки на главной странице"""
        return self.wait_for_element(StellarBurgersHomePageLocators.NAME_BUN_FLUORESCENT).text

    @allure.step("Открытие главной страницы сайта")
    def open_home_page(self):
        """Открытие главной страницы сайта"""
        self.navigate(DOMEN, StellarBurgersHomePageLocators.DIV_BUNS)

    @allure.step("Клик по флуоресцентной булочке")
    def click_fluorescent_bun(self):
        """Клик по элементу флуоресцентной булочки и ожидание открытия модального окна"""
        self.action_click(StellarBurgersHomePageLocators.BUN_FLUORESCENT,
                          StellarBurgersHomePageLocators.BUN_FLUORESCENT)
