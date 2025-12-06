import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.scooter_logo)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(HeaderLocators.yandex_logo)

    @allure.step('Нажать на кнопку заказа в шапке')
    def click_top_order_button(self):
        self.click_element(HeaderLocators.order_button)