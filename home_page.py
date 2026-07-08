from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    DASHBOARD = (By.XPATH, "//*[contains(text(),'Dashboard')]")
    PROFILE_ICON = (By.XPATH, "//*[contains(text(),'Sumitha V')]")
    LOGOUT = (By.XPATH, "//*[contains(text(),'Log out')]")

    def verify_login(self):
        actual = self.get_text(self.DASHBOARD)
        assert actual == "Dashboard"

    def perform_operation(self):
        print("Page Title:", self.get_title())
        print("Current URL:", self.get_current_url())

    def logout(self):
        self.driver.execute_script("arguments[0].click();",
                                   self.wait.until(
                                       EC.element_to_be_clickable(self.PROFILE_ICON)
                                   ))

        self.driver.execute_script("arguments[0].click();",
                                   self.wait.until(
                                       EC.element_to_be_clickable(self.LOGOUT)
                                   ))

    def close_browseroperation(self):
        self.close_browser()