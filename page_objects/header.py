from page_objects.base_page import BasePage
from locators.header_locators import StellarBurgersHeader



class Header(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def click_link_personal_area(self):
        self.action_click(StellarBurgersHeader.PERSONAL_AREA_BUTTON,
                          StellarBurgersHeader.LINK_LOGO)

    def click_link_constructor(self):
        self.action_click(StellarBurgersHeader.LINK_CONSTRUCTOR,
                          StellarBurgersHeader.LINK_LOGO)

    def click_link_order_feed(self):
        self.action_click(StellarBurgersHeader.LINK_ORDER_FEED,
                          StellarBurgersHeader.LINK_LOGO)
