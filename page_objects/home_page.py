from page_objects.base_page import BasePage
from locators.home_page_locators import StellarBurgersHomePageLocators
from locators.ingredient_modal_locators import StellarBurgersIngredientModal
from config import DOMEN


class HomePage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def open_home_page(self):
        self.navigate(DOMEN, StellarBurgersHomePageLocators.DIV_BUNS)

    def click_fluorescent_bun(self):
        self.action_click(StellarBurgersHomePageLocators.BUN_FLUORESCENT, StellarBurgersIngredientModal.MODAL_TITLE)

    def click_close_modal_ingredient(self):
        self.action_click(StellarBurgersIngredientModal.MODAL_BUTTON_CLOSE,
                          StellarBurgersHomePageLocators.BUN_FLUORESCENT)
