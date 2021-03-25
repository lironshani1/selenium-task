from selenium.webdriver.common.by import By
import pages.mainpage
from newclass import NewClass


class MyAccount(NewClass):
    def __init__(self, driver):
        self.driver = driver

    locator_dictionary = {
        "home": (By.CLASS_NAME, 'home')
    }

    def home(self):
        NewClass._find_by(self, *self.locator_dictionary['home']).click()
        return pages.mainpage.MainPage(self.driver)
