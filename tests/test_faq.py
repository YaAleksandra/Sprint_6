import pytest
import allure

from pages.main_page import MainPage
from urls import Urls
from data import Questions


class TestFAQs:

    @allure.title('Проверка списка вопросов в разделе "Вопросы о важном"')
    @allure.description('Последовательно нажимаем на каждый вопрос и проверяем, что в ответе верный текст. Тексты в файле data.')
    @pytest.mark.parametrize ('question_number,answer_text', Questions.answers)
    def test_faq_answers(self, question_number, answer_text, firefox_create_close):
        driver = firefox_create_close
        main_page = MainPage(driver)
        main_page.open(Urls.main_page)
        main_page.scroll_to_faq_question(question_number)
        main_page.click_faq_question(question_number)
        actual_text = main_page.get_faq_answer_text(question_number)
        
        assert actual_text == answer_text