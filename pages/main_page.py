import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Перейти к вопросу с переданным номером")
    def scroll_to_faq_question(self, question_number):
        self.scroll_to_element(MainPageLocators.faq_question(question_number))

    @allure.step('Кликнуть на вопрос с переданным номером')
    def click_faq_question(self, question_number):
        self.click_element(MainPageLocators.faq_question(question_number))

    @allure.step('Проверка текста ответа на вопрос с переданным номером')
    def get_faq_answer_text(self, question_number):
        return self.get_element_text(MainPageLocators.faq_answer(question_number))

    @allure.step('Кликнуть на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        self.click_element(MainPageLocators.order_button)