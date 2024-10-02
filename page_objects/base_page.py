from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url: str, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    def enter_test(self, locator, text: str):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def action_click(self, element_click, expected_element):
        self.driver.find_element(*element_click).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(expected_element))

