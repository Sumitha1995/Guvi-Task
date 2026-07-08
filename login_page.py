from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.XPATH, "//input[@placeholder='Enter your mail']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Enter your password ']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Invalid email!')]")

    def open_login_page(self):
        self.open_url("https://www.zenclass.in/login")

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)