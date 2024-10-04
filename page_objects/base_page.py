from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    @allure.step("Переход по URL и ожидание загрузки элемента: {locator}")
    def navigate(self, url: str, locator):
        """Переход на страницу и ожидание появления элемента"""
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def enter_test(self, locator, text: str):
        """Очистка и ввод текста в элемент"""
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Клик по элементу: {element_click} и ожидание элемента: {expected_element}")
    def action_click(self, element_click, expected_element):
        """Клик по элементу и ожидание загрузки нового элемента"""
        self.driver.find_element(*element_click).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(expected_element))
