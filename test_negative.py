from selenium import webdriver

def test_wrong_title():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert driver.title != "Amazon"

    driver.quit()