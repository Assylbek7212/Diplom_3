# page_objects/base_page.py
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

    @allure.step("Получение списка элементов: {locator}")
    def find_elements(self, locator, timeout=10):
        """Получение списка элементов на странице"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Переход по URL: {url}")
    def navigate(self, url, expected_element=None):
        """Открытие указанного URL и ожидание загрузки элемента"""
        self.driver.get(url)
        if expected_element:
            self.wait_for_element(expected_element)

    @allure.step("Ввод текста: {text} в элемент {locator}")
    def enter_text(self, locator, text):
        """Ввод текста в указанный элемент"""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Клик по элементу: {locator}")
    def action_click(self, locator, expected_element=None):
        """Клик по элементу и ожидание загрузки другого элемента, если указан"""
        element = self.wait_for_element(locator)
        element.click()
        if expected_element:
            self.wait_for_element(expected_element)

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url

    @allure.step("Проверка, что пользователь находится на странице с URL: {url}")
    def is_at_url(self, url):
        """Проверка, что текущий URL совпадает с ожидаемым"""
        return self.get_current_url() == url

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ожидание исчезновения элемента со страницы"""
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Проверка, что элемент виден: {locator}")
    def is_element_visible(self, locator, timeout=10):
        """Проверка, что элемент виден на странице"""
        try:
            return self.wait_for_element(locator, timeout).is_displayed()
        except:
            return False

    @allure.step("Проверка, что элемент невиден: {locator}")
    def is_element_invisible(self, locator, timeout=10):
        """Проверка, что элемент невиден на странице"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except:
            return False

    @allure.step("Ожидание исчезновения перекрывающего элемента: {locator}")
    def wait_for_overlay_to_disappear(self, locator, timeout=10):
        """Ожидание исчезновения перекрывающего элемента"""
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
