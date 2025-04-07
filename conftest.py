import pytest
from selenium import webdriver
from config.config import Config


@pytest.fixture(scope="function")
# @pytest.fixture(scope="module") // for module based, means to launch at the first function of the page and end at
# the last function
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    yield driver
    driver.quit()
