import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_drag_drop_positive():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://jqueryui.com/droppable/")

    # Switch to iframe
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    # Locate elements
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    # Drag and Drop using ActionChains
    ActionChains(driver).drag_and_drop(source, target).perform()

    # Validating
    assert target.text == "Dropped!"
    time.sleep(5)
    driver.quit()


def test_drag_drop_negative():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://jqueryui.com/droppable/")

    # Switch to iframe
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    target = driver.find_element(By.ID, "droppable")

    # Validation before drag and drop
    assert target.text == "Drop here"
    time.sleep(5)
    driver.quit()