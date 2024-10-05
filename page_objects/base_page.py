from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на страницу: {url}")
    def go_to(self, url):
        """Переход на указанную страницу по URL"""
        self.driver.get(url)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element(self, locator, timeout=10):
        """Ожидание видимости элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание появления элемента на странице: {locator}")
    def wait_for_element_to_appear(self, locator, timeout=10):
        """Ожидание появления элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Прокрутка к элементу: {locator}")
    def scroll_to_element(self, locator):
        """Прокрутка страницы до указанного элемента"""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url

    @allure.step("Проверка, что пользователь находится на странице с URL: {url}")
    def is_at_url(self, url):
        """Проверка, что текущий URL совпадает с ожидаемым"""
        return self.get_current_url() == url

    @allure.step("Выполнение JavaScript кода: {script}")
    def execute_script(self, script, *args):
        """Выполнение JavaScript кода на текущей странице"""
        return self.driver.execute_script(script, *args)
