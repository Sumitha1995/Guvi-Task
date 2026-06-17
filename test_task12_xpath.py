import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_task12_xpath():

    # Launch Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open GUVI website
    driver.get("https://www.guvi.in/")
    time.sleep(5)

    # Find parent element of Courses menu
    parent = driver.find_element(By.XPATH,"//p[text()='Courses']/parent::*")
    print("Parent:", parent.tag_name)

    # Find first child element
    first_child = driver.find_element(By.XPATH,"//p[text()='Courses']/parent::*/*[1]")
    print("First Child:", first_child.tag_name)

    # Find second sibling element
    second_sibling = driver.find_element(By.XPATH,"//p[text()='Courses']/parent::*/following-sibling::*[2]")
    print("Second Sibling:", second_sibling.text)

    # Find parent elements containing href attribute
    href_parent = driver.find_elements(By.XPATH,"//a[@href]/parent::*")
    print("Parents with href:", len(href_parent))

    # Find all ancestor elements
    ancestors = driver.find_elements(By.XPATH,"//p[text()='Courses']/ancestor::*")
    print("Ancestors:", len(ancestors))

    # Find all following siblings
    following = driver.find_elements(By.XPATH,"//p[text()='Courses']/parent::*/following-sibling::*")
    print("Following Siblings:", len(following))

    # Find all preceding elements
    preceding = driver.find_elements(By.XPATH,"//a[contains(text(),'Login')]/preceding::*")
    print("Preceding Elements:", len(preceding))

    # Close browser
    driver.quit()