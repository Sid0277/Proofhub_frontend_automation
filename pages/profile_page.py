# pages/profile_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    PROFILE_NAME = (By.ID, "profile-name")
    EDIT_BUTTON = (By.ID, "edit-button")
    SAVE_BUTTON = (By.ID, "save-button")

    def get_profile_name(self):
        return self.get_text(self.PROFILE_NAME)

    def edit_profile(self, new_name):
        self.click(self.EDIT_BUTTON)
        self.send_keys(self.PROFILE_NAME, new_name)
        self.click(self.SAVE_BUTTON)