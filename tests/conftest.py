import pytest

from page_objects.register_page import RegisterPage
from page_objects.login_page import LoginPage
from selenium import webdriver
from helpers import get_faker_user
from config import DOMEN


def _get_driver(name):
    if name == "chrome":
        return webdriver.Chrome()
    elif name == "firefox":
        return webdriver.Firefox()
    else:
        raise TypeError("Driver is not found")


@pytest.fixture(params=["chrome", "firefox"])
def web_driver(request):
    driver = _get_driver(request.param)
    driver.get(DOMEN)
    yield driver
    driver.quit()


@pytest.fixture
def signup(web_driver):
    name = get_faker_user()["name"]
    email = get_faker_user()["email"]
    password = get_faker_user()["password"]
    register_page = RegisterPage(web_driver)
    register_page.signup(name, email, password)
    return {"email": email, "password": password}


@pytest.fixture
def login(web_driver, signup):
    login_page = LoginPage(web_driver)
    login_page.login(signup["email"], signup["password"])
    return signup

