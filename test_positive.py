# Importing the libraries

from selenium import webdriver
from selenium.webdriver.common.by import By

#pytest function to test the title
def test_title():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"

    driver.quit()

#pytest funtion to test the homepage url
def test_homepage_url():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    #verifying the url
    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()

#pytest dashboard
def test_dashboard_url():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()
