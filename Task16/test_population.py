from pages.population_page import PopulationPage


def test_world_population(driver):

    population = PopulationPage(driver)

    population.open_website()

    population.display_population()