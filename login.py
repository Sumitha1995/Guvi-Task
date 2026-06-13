
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(4)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(2)

driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(2)

driver.find_element(By.ID,"login-button").click()
time.sleep(4)

print("Title Of The webpage :", driver.title)
print("Current URL Of The Webpage :", driver.current_url)

# Copy webpage content and save into text file

page_content = driver.find_element(By.TAG_NAME, "body").text

with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content)

print("Webpage content saved successfully!")