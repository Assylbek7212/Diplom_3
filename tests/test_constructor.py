import allure

from page_objects.home_page import HomePage
from locators.ingredient_modal_locators import StellarBurgersIngredientModal
from locators.home_page_locators import StellarBurgersHomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    @allure.title('Открытие модального окна ингредиента')
    def test_click_on_ingredient(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_fluorescent_bun()
        name_ingredient = web_driver.find_element(*StellarBurgersHomePageLocators.NAME_BUN_FLUORESCENT).text
        name_ingredient_in_modal = web_driver.find_element(*StellarBurgersIngredientModal.MODAL_NAME_INGREDIENT).text
        assert web_driver.find_element(*StellarBurgersIngredientModal.MODAL_TITLE).is_displayed()
        assert name_ingredient == name_ingredient_in_modal

    @allure.title('Закрытие модального окна ингредиента')
    def test_click_on_ingredient(self, web_driver):
        home_page = HomePage(web_driver)
        home_page.click_fluorescent_bun()
        assert web_driver.find_element(*StellarBurgersIngredientModal.MODAL_TITLE).is_displayed()
        home_page.click_close_modal_ingredient()
        assert WebDriverWait(web_driver, 10).until(expected_conditions.invisibility_of_element_located(
            StellarBurgersIngredientModal.MODAL_TITLE)) is not None




