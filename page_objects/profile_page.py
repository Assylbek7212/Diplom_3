import allure
from page_objects.base_page import BasePage
from locators.profile_page_locators import StellarBurgersProfilePageLocators
from config import URL


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StellarBurgersProfilePageLocators

    @allure.step("Открытие страницы заказов пользователя")
    def open_user_orders(self):
        """Переход на страницу заказов пользователя в личном кабинете"""
        self.navigate(URL.PERSONAL_AREA.value, self.locators.USER_ORDERS)

    @allure.step("Получение списка заказов пользователя")
    def get_user_orders(self):
        """Возвращает список заказов пользователя на странице личного кабинета"""
        orders = self.find_elements(self.locators.USER_ORDERS)
        return [order.text for order in orders]

    @allure.step("Переход на вкладку профиля")
    def go_to_profile_tab(self):
        """Переход на вкладку профиля"""
        self.action_click(self.locators.TAB_PROFILE)

    @allure.step("Ввод нового имени пользователя: {name}")
    def enter_name(self, name):
        """Ввод нового имени пользователя"""
        self.clear_and_enter_text(self.locators.INPUT_NAME, name)

    @allure.step("Сохранение изменений профиля")
    def click_save_button(self):
        """Клик по кнопке 'Сохранить'"""
        self.action_click(self.locators.BUTTON_SAVE)

    @allure.step("Получение имени пользователя")
    def get_name(self):
        """Получение текущего имени пользователя"""
        return self.get_element_text(self.locators.INPUT_NAME)

    @allure.step("Выход из аккаунта")
    def logout(self):
        """Клик по кнопке выхода из аккаунта"""
        self.action_click(self.locators.LOGOUT_BUTTON)
