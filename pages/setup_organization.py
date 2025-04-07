import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SetupOrganizationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.organization_name = (By.ID, "input-4")
        self.workspace_name = (By.ID, "input-6")
        self.proceedButton = (
            By.XPATH, "//*[@id='app']/div/div/div/div/div/div[2]/div/div/form/div[3]/button")

    def setup_organization(self, org_name, works_name):
        self.input_text(*self.organization_name, org_name)
        self.input_text(*self.workspace_name, works_name)
        self.click(*self.proceedButton)
        time.sleep(20)
