from selenium.webdriver.common.by import By

class IngredientPage:
    def __init__(self, driver):
        self.driver = driver
        self.ingredient_locator = (By.XPATH, "//p[contains(text(),'Флюоресцентный бургер')]")
        self.counter_locator = (By.XPATH, "//span[@class='counter__num']")

    def add_ingredient(self):
        ingredient = self.driver.find_element(*self.ingredient_locator)
        ingredient.click()

    def is_counter_increased(self):
        counter = self.driver.find_element(*self.counter_locator)
        return int(counter.text) > 0
