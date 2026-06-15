import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Positive test case to validate successful login
def test_guvi_login():

    #launch the chrome browser
    driver=webdriver.Chrome()
    driver.maximize_window()

    #Open GUVI website
    driver.get("https://www.guvi.in/")

    driver.find_element(By.ID,"login-btn").click()
    time.sleep(2)

    expected_url = "https://www.guvi.in/sign-in/"
    actual_url = driver.current_url
    assert actual_url.startswith(expected_url)

    username = driver.find_element(By.ID, "email")

    assert username.is_displayed()
    assert username.is_enabled()

    password = driver.find_element(By.ID, "password")

    assert password.is_displayed()
    assert password.is_enabled()

    driver.find_element(By.ID, "email").send_keys("validusername@gmail.com")

    driver.find_element(By.ID, "password").send_keys("Validpassword")

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(4)

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    driver.quit()

#Negative test case to validate login with invalid credentials
def test_guvi_invalid_login():

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://www.guvi.in/")

        driver.find_element(By.ID, "login-btn").click()

        driver.find_element(By.ID, "email").send_keys("wrong@gmail.com")

        driver.find_element(By.ID, "password").send_keys("wrong123")

        driver.find_element(By.ID, "login-btn").click()
        time.sleep(4)

        actual1_url = driver.current_url

        # Login should fail and user should remain on sign-in page
        assert "sign-in" in actual1_url

        driver.quit()