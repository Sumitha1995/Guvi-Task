import pytest
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.login_page import LoginPage
from Utilities.excel_utils import ExcelUtils

path = "Test Data/login_data.xlsx"
sheet_name = "Sheet1"


@pytest.mark.parametrize("row", range(2, 7))
def test_login(driver, row):

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)

    username = ExcelUtils.read_data(path, sheet_name, row, 2)
    password = ExcelUtils.read_data(path, sheet_name, row, 3)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    current_datetime = datetime.now()

    ExcelUtils.write_data(
        path, sheet_name, row, 4,
        current_datetime.strftime("%d-%m-%Y")
    )

    ExcelUtils.write_data(
        path, sheet_name, row, 5,
        current_datetime.strftime("%H:%M:%S")
    )

    ExcelUtils.write_data(
        path, sheet_name, row, 6,
        "Smitha"
    )

    wait = WebDriverWait(driver, 10)

    try:
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']")
            )
        )

        ExcelUtils.write_data(
            path, sheet_name, row, 7,
            "PASS"
        )

    except:
        ExcelUtils.write_data(
            path, sheet_name, row, 7,
            "FAIL"
        )