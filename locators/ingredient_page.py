from selenium.webdriver.common.by import By


class StellarBurgersIngredientPage:
    INGREDIENT_MODAL = (By.XPATH, "//p[contains(text(),'Флюоресцентный бургер')]")
    COUNTER_LOCATOR= (By.XPATH, "//span[@class='counter__num']")
