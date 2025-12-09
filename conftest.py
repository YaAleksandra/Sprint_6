
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def firefox_create_close ():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

