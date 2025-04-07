# import pytest
# from pages.login_page import LoginPage
# from selenium import webdriver
# from config.config import Config
#
# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
# def test_valid_login(setup):
#     driver = setup
#     driver.get(Config.BASE_URL + "/login")
#     login_page = LoginPage(driver)
#     login_page.login("valid_email@example.com", "valid_password")
#     assert "Dashboard" in driver.title
#


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# tests/test_login.py
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.order(1)
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.login("admin", "password")
    assert "Dashboard" in browser.title


@pytest.mark.order(2)
def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.login("wrong_user", "wrong_password")
    error_message = login_page.get_text((By.ID, "error-message"))
    assert "Invalid credentials" in error_message
