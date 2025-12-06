from selenium.webdriver.common.by import By


class MainPageLocators:

    order_button = (By.XPATH, '//div[contains(@class,"Home_FinishButton")]/button')

    faq_section = (By.XPATH, '//*[contains(text(), "Вопросы о важном")]')
    faq_container = (By.XPATH, '//div[@class="accordion"]')

    @staticmethod
    def faq_question(question_number):
        return By.XPATH, f'//*[@id="accordion__heading-{question_number}"]'
    
    @staticmethod
    def faq_answer(question_number):
        return By.XPATH, f'//*[@id="accordion__panel-{question_number}"]'