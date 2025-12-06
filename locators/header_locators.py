from selenium.webdriver.common.by import By


class HeaderLocators:

    scooter_logo = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
    yandex_logo = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')
    order_button = (By.XPATH, '//div[contains(@class,"Header_Nav")]/button')