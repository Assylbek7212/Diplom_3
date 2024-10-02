from page_objects.base_page import BasePage
from locators.personal_area_locators import StellarBurgersPersonalArea
from locators.login_locators import StellarBurgersLoginLocators


class PersonalArea(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def click_button_exit(self):
        self.action_click(StellarBurgersPersonalArea.BUTTON_EXIT,
                          StellarBurgersLoginLocators.TITLE_FORM)