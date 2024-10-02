from selenium.webdriver.common.by import By


class StellarBurgersHeader:
    PERSONAL_AREA_BUTTON = (By.XPATH, "//a[.='Личный Кабинет']")  # Кнопка "личный кабинет" в шапке
    LINK_LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")  # Логотип
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']/parent::a")  # Ссылка на конструктор
    LINK_ORDER_FEED = (By.XPATH, "//p[text() = 'Лента Заказов']/parent::a")  # Ссылка на ленту заказов

