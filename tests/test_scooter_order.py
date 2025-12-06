import pytest
import allure
import time
from data import Credentials, RentDetails
from urls import Urls

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.header import Header
from locators.header_locators import HeaderLocators
from pages.order_page import OrderPage


class TestScooterOrder:

    @allure.title('Позитивный сценарий создания заказа с двумя наборами данных и двумя кнопками входа')
    @allure.description('Сценарий теста: нажать кнопку "Заказать", заполнить форму персональных данных, заполнить форму деталей аренды, подтвердить заказ на всплывающем окне и получить сообщения о создании заказа.')
    @pytest.mark.parametrize('entry_point,credentials,rent_details',[
        [HeaderLocators.order_button, Credentials.credentials_1, RentDetails.rent_details_1],
        [MainPageLocators.order_button, Credentials.credentials_2, RentDetails.rent_details_2]
        ])
    def test_order_creation_flow(self, entry_point, credentials, rent_details, firefox_create_close):
        driver = firefox_create_close
        driver.get(Urls.main_page)
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        
        main_page.scroll_to_element(entry_point)
        main_page.click_element(entry_point)

        order_page.fill_personal_info(
            credentials.get('name'), 
            credentials.get('surname'), 
            credentials.get('address'), 
            credentials.get('metro_station'), 
            credentials.get('phone_number'))
        
        order_page.click_next_button()
        order_page.fill_rental_details(
            rent_details.get('start_date'), 
            rent_details.get('duration'), 
            rent_details.get('color_black'), 
            rent_details.get('color_grey'), 
            rent_details.get('comment'))

        order_page.click_order_submit_button()
        order_page.wait_for_confirmation_modal()
        order_page.cancel_order_confirmation()

        order_page.click_order_submit_button()
        order_page.wait_for_confirmation_modal()
        order_page.confirm_order()

        assert order_page.is_order_confirmed()

    @allure.title('Проверка нажатия на лого Самоката')
    @allure.description('Проверка, что при нажатии на лого Самоката приложение переводит на главную страницу.')
    def test_scooter_logo_redirects_to_main_page(self, firefox_create_close):
        driver = firefox_create_close
        driver.get(Urls.order_page)
        header = Header(driver)
        header.click_scooter_logo()

        assert header.get_current_url() == Urls.main_page

    @allure.title("Проверка нажатия на лого Яндекса")
    @allure.description("Проверка, что при нажатии на лого Яндекса приложение переводит на страницу Дзена")
    def test_yandex_logo_redirects_to_dzen(self, firefox_create_close):
        driver = firefox_create_close
        driver.get(Urls.order_page)
        header = Header(driver)
        header.click_yandex_logo()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        current_url = driver.current_url

        assert "dzen.ru" in current_url, f"Ожидался dzen.ru, получен: {current_url}"