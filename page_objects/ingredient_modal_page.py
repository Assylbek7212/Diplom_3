import allure
from page_objects.base_page import BasePage
from locators.ingredient_modal_locators import StellarBurgersIngredientModal


class IngredientModalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка, что модальное окно ингредиента открыто")
    def is_modal_open(self):
        """Проверка открытия модального окна"""
        return self.wait_for_element(StellarBurgersIngredientModal.MODAL_TITLE).is_displayed()

    @allure.step("Получение названия ингредиента из модального окна")
    def get_ingredient_name_in_modal(self):
        """Получение названия ингредиента, отображаемого в модальном окне"""
        return self.wait_for_element(StellarBurgersIngredientModal.MODAL_NAME_INGREDIENT).text

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal(self):
        """Закрытие модального окна ингредиента"""
        self.action_click(StellarBurgersIngredientModal.MODAL_BUTTON_CLOSE, StellarBurgersIngredientModal.MODAL_TITLE)
