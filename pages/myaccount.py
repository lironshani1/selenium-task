from conftest import improved_find_by
from selenium.webdriver.common.by import By
from pages import mainpage


class MyAccount:
    def __init__(self, driver):
        self.driver = driver

    locator_dictionary = {
        "home": (By.CLASS_NAME, 'home')
    }

    def home(self):
        improved_find_by(self.driver, self.locator_dictionary['home'][0], 10, self.locator_dictionary['home'][1]).click()
        return mainpage.MainPage(self.driver)
