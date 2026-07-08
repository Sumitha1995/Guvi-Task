from tests.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_login_logout():

    driver = get_driver()

    login = LoginPage(driver)
    home = HomePage(driver)

    try:
        # Open Login Page
        login.open_login_page()

        # Login with valid credentials
        login.login("USER NAME", "PASSWORD")

        # Verify Login
        home.verify_login()

        # Print Title and URL
        home.perform_operation()

        # Logout
        home.logout()

    finally:
        home.close_browseroperation()


def test_invalid_login():

    driver = get_driver()

    login = LoginPage(driver)

    try:
        # Open Login Page
        login.open_login_page()

        # Login with invalid credentials
        login.login("abc@gmail.com", "WrongPassword123")

        # Verify Error Message
        actual = login.get_error_message()

        assert "Invalid email!" in actual

    finally:
        driver.quit()