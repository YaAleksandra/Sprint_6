import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    @allure.step("Создание экземпляра класса BasePage")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Переход к элементу")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    @allure.step("Ввод переданного значения в элемент")
    def fill_field(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Ожидание и проверка, что элемент стал виден")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Вернуть текущий url драйвера")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание нового окна")
    def wait_for_new_window_opened(self, original_window, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len([original_window])
        )

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self, original_window):
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                return window_handle
        raise Exception("Новое окно не найдено")

    @allure.step("Ожидание URL содержащего текст")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step("Ожидание открытия новой вкладки")
    def wait_for_number_of_windows_to_be(self, number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) == number
        )