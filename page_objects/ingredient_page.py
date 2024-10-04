import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class IngredientPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Локаторы вынесены в отдельные атрибуты
        self.ingredient_locator = (By.XPATH, "//p[contains(text(),'Флюоресцентный бургер')]")
        self.counter_locator = (By.XPATH, "//span[@class='counter__num']")

    @allure.step("Добавление ингредиента 'Флюоресцентный бургер' в конструктор")
    def add_ingredient(self):
        """Клик по ингредиенту 'Флюоресцентный бургер' для добавления в конструктор"""
        ingredient = self.wait_for_element(self.ingredient_locator)  # Ожидание появления элемента
        ingredient.click()  # Клик по элементу

    @allure.step("Проверка увеличения счетчика ингредиентов")
    def is_counter_increased(self):
        """Проверка, увеличился ли счетчик добавленного ингредиента"""
        counter = self.wait_for_element(self.counter_locator)  # Ожидание появления счетчика
        return int(counter.text) > 0  # Проверка значения счетчика
