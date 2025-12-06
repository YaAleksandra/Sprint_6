from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    # первая часть заказа
    name_input = (By.XPATH, '//div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Имя")]')
    surname_input = (By.XPATH, '//div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Фамилия")]')
    address_input = (By.XPATH, '//div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Адрес")]')
    metro_input = (By.XPATH, '//div[contains(@class, "Order_Form")]//input[contains(@placeholder, "метро")]')
    metro_dropdown_first_option = (By.XPATH, '//div[contains(@class, "Order_Form")]//*[contains(@class, "select-search__select")]//button[1]')
    phone_input = (By.XPATH, '//div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Телефон")]')
    next_button = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button')

    # вторая часть заказа
    order_content = (By.XPATH, '//div[contains(@class, "Order_Content")]')
    date_input = (By.XPATH, '//div[@class= "react-datepicker__input-container"]//input')
    period_dropdown = (By.XPATH, '//div[contains(@class, "Dropdown-root")]')
    color_black_checkbox = (By.ID, 'black')
    color_grey_checkbox = (By.ID, 'grey')
    comment_input = (By.XPATH, '//div[contains(@class, "Order_Form")]//div[contains(@class, "Input_InputContainer")]//input')
    back_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[contains(text(), "Назад")]')
    submit_order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[contains(text(), "Заказать")]')

    @staticmethod
    def period_option(days):
        return By.XPATH, f'//div[contains(@class, "Dropdown-option")][{days}]'

    # окно подтверждения заказа
    confirmation_modal = (By.XPATH, '//div[contains(@class, "Modal")]')
    confirmation_no_button = (By.XPATH, '//div[contains(@class, "Modal")]//button[contains(text(), "Нет")]')
    confirmation_yes_button = (By.XPATH, '//div[contains(@class, "Modal")]//button[contains(text(), "Да")]')
    order_success_header = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')