import allure
from page_objects.base_page import BasePage
from locators.ingredient_page import StellarBurgersIngredientPage


class IngredientPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Добавление ингредиента 'Флюоресцентный бургер' в конструктор")
    def add_ingredient(self):
        """Клик по ингредиенту 'Флюоресцентный бургер' для добавления в конструктор"""
        ingredient = self.wait_for_element(StellarBurgersIngredientPage.INGREDIENT_MODAL)
        ingredient.click()

    @allure.step("Проверка увеличения счетчика ингредиентов")
    def is_counter_increased(self):
        """Проверка, увеличился ли счетчик добавленного ингредиента"""
        counter = self.wait_for_element(StellarBurgersIngredientPage.COUNTER_LOCATOR)
        return int(counter.text) > 0
