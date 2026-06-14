#importing the required libraries

from selenium import webdriver

#pytest function for wrong title
def test_wrong_title():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    #verifying the title
    assert driver.title != "Amazon"

    driver.quit()
