from selenium import webdriver
from selenium.webdriver.common.by import By

def test_title():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"

    driver.quit()


def test_homepage_url():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()


def test_dashboard_url():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()