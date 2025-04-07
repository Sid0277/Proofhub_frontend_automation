from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.user_display_name = (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/main/div[1]/div[1]/div[1]/div[2]/span")
        # self.username_field = (By.ID, "work_email")
        # self.carry_forward = (By.ID, "carryForwardBtn")
        # self.password_field = (By.ID, "password")
        # self.signup_button = (By.ID, "formSubmit")

    # def signup(self, email, password):
    #     self.input_text(*self.username_field, email)
    #     self.click(*self.carry_forward)
    #     self.input_text(*self.password_field, password)
    #     self.click(*self.signup_button)
