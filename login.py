# Import required libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

 # Launch Chrome browser
driver=webdriver.Chrome()

 # Maximize browser window
driver.maximize_window()

 # Open Swag Labs website
driver.get("https://www.saucedemo.com/")
time.sleep(4)

#Finding element by ID and sending user name
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(2)

#Finding element by ID and sending Password
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(2)

#Finding element by ID and clicking Login button
driver.find_element(By.ID,"login-button").click()
time.sleep(4)

#Fetching Title of the webpage
print("Title Of The webpage :", driver.title)

#Fetching Current URL of the webpage
print("Current URL Of The Webpage :", driver.current_url)

# Copy webpage content and save into text file
page_content = driver.find_element(By.TAG_NAME, "body").text

# Writting content in a file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content)

print("Webpage content saved successfully!")
