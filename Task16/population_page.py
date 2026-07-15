import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    population = (
        By.XPATH,
        "//app-counter//div[contains(@class,'counter-ticker')]"
    )

    def open_website(self):
        self.driver.get(
            "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"
        )

    def display_population(self):

        self.wait.until(
            EC.visibility_of_element_located(self.population)
        )

        print("\nPress CTRL + C to stop...\n")

        try:
            while True:
                population_count = self.driver.find_element(*self.population).text
                print("Current Population :", population_count)
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nExecution Stopped.")