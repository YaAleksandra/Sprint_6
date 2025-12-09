import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Создание экземпляра OrderPage")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ввести переданное значение в поле Имя")
    def enter_name(self, name):
        self.fill_field(OrderPageLocators.name_input, name)

    @allure.step("Ввести переданное значение в поле Фамилия")
    def enter_surname(self, surname):
        self.fill_field(OrderPageLocators.surname_input, surname)

    @allure.step("Ввести переданное значение в поле Адрес")
    def enter_address(self, address):
        self.fill_field(OrderPageLocators.address_input, address)

    @allure.step("Ввести переданное значение в поле Станция метро и нажать кнопку")
    def enter_metro_station(self, metro_station):
        self.fill_field(OrderPageLocators.metro_input, metro_station)
        self.click_element(OrderPageLocators.metro_dropdown_first_option)

    @allure.step("Ввести переданное значение в поле Телефон")
    def enter_phone_number(self, phone_number):
        self.fill_field(OrderPageLocators.phone_input, phone_number)

    @allure.step("Заполнить все поля формы ввода персональных данных")
    def fill_personal_info(self, name, surname, address, metro_station, phone):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro_station(metro_station)
        self.enter_phone_number(phone)

    @allure.step("Нажать на кнопку Далее на форме ввода персональных данных")
    def click_next_button(self):
        self.click_element(OrderPageLocators.next_button)

    @allure.step("Ввести переданное значение в поле Дата")
    def enter_rental_date(self, date):
        self.fill_field(OrderPageLocators.date_input, date)
        self.click_element(OrderPageLocators.order_content)

    @allure.step("Выбрать длительность аренды из выпадающего списка")
    def select_rental_period(self, days):
        self.click_element(OrderPageLocators.period_dropdown)
        self.click_element(OrderPageLocators.period_option(days))

    @allure.step("Выбрать цвет в чекбоксе")
    def select_scooter_colors(self, black_selected, grey_selected):
        if black_selected:
            self.click_element(OrderPageLocators.color_black_checkbox)
        if grey_selected:
            self.click_element(OrderPageLocators.color_grey_checkbox)

    @allure.step("Ввести комментарий")
    def enter_comment_for_courier(self, comment):
        self.fill_field(OrderPageLocators.comment_input, comment)

    @allure.step("Заполнить все поля формы ввода деталей аренды")
    def fill_rental_details(self, date, duration, black_selected, grey_selected, comment):
        self.enter_rental_date(date)
        self.select_rental_period(duration)
        self.select_scooter_colors(black_selected, grey_selected)
        self.enter_comment_for_courier(comment)

    @allure.step("Нажать на кнопку Назад")
    def click_back_button(self):
        self.click_element(OrderPageLocators.back_button)

    @allure.step("Нажать на кнопку Заказать")
    def click_order_submit_button(self):
        self.click_element(OrderPageLocators.submit_order_button)

    @allure.step("Подождать появления формы подтверждения заказа")
    def wait_for_confirmation_modal(self):
        self.wait_for_element(OrderPageLocators.confirmation_modal)

    @allure.step("Нажать на кнопку Да в форме подтверждения заказа")
    def confirm_order(self):
        self.click_element(OrderPageLocators.confirmation_yes_button)

    @allure.step("Нажать на кнопку Нет в форме подтверждения заказа")
    def cancel_order_confirmation(self):
        self.click_element(OrderPageLocators.confirmation_no_button)

    @allure.step("Проверить, что появилось окно подтверждения заказа")
    def is_order_confirmed(self):
        return self.is_element_visible(OrderPageLocators.order_success_header)