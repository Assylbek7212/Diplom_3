from selenium.webdriver.common.by import By


class StellarBurgersIngredientModal:
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div") # Модальное окно ингрелиентов
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']") # Заголовок модалки
    MODAL_NAME_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/p") # Название ингредиента
    # кнопка закрытия модального окна ингредиентов
    MODAL_BUTTON_CLOSE = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/following::button[1]")

