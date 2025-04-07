from utils.helpers import BasePage
from selenium.webdriver.common.by import By

# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.email_field = (By.ID, "email")
#         self.password_field = (By.ID, "password")
#         self.login_button = (By.ID, "login")
#
#     def login(self, email, password):
#         self.input_text(*self.email_field, email)
#         self.input_text(*self.password_field, password)
#         self.click(*self.login_button)

# pages/login_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login")

    def login(self, email, password):
        self.send_keys(self.email_field, email)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)