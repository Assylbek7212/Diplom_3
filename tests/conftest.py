import pytest
from page_objects.register_page import RegisterPage
from page_objects.login_page import LoginPage
from selenium import webdriver
from helpers import get_faker_user
from config import DOMEN


def _get_driver(name):
    """Функция для инициализации драйвера на основе переданного параметра."""
    if name == "chrome":
        return webdriver.Chrome()
    elif name == "firefox":
        return webdriver.Firefox()
    else:
        raise TypeError("Driver is not found")


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def web_driver(request):
    """Фикстура для инициализации веб-драйвера с параметрами 'chrome' и 'firefox'."""
    driver = _get_driver(request.param)
    driver.maximize_window()  # Открыть окно браузера в полном размере
    driver.get(DOMEN)  # Открыть URL
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def signup(web_driver):
    """Фикстура для регистрации нового пользователя и возврата его учетных данных."""
    user = get_faker_user()  # Генерация тестовых данных пользователя
    name = user["name"]
    email = user["email"]
    password = user["password"]

    register_page = RegisterPage(web_driver)
    register_page.signup(name, email, password)

    return {"email": email, "password": password}


@pytest.fixture
def login(web_driver, signup):
    """Фикстура для выполнения логина с учетными данными зарегистрированного пользователя."""
    login_page = LoginPage(web_driver)
    login_page.login(signup["email"], signup["password"])
    return signup
