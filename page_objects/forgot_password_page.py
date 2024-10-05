import allure
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.forgot_password_locators import StellarBurgersForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StellarBurgersForgotPasswordLocators

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        """Переход на страницу восстановления пароля"""
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    @allure.step("Ввод email для восстановления пароля: {email}")
    def enter_email(self, email):
        """Ввод email в поле восстановления пароля"""
        self.enter_text(self.locators.EMAIL, email)

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_button_restore_password(self):
        """Клик по кнопке 'Восстановить пароль' на странице восстановления пароля"""
        # Явное ожидание исчезновения перекрывающего элемента перед кликом
        self.wait_for_element_to_disappear(self.MODAL_OVERLAY)
        self.action_click(self.locators.BUTTON_RESTORE_PASSWORD)
