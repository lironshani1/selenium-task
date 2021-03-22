from conftest import improved_find_by
from selenium.webdriver.common.by import By
from pages.myaccount import MyAccount


class AuthPage:
    def __init__(self, driver):
        self.driver = driver

    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "submit": (By.ID, 'SubmitLogin')
    }

    def login(self, user_name, password):
        improved_find_by(self.driver, self.locator_dictionary['email'][0], 10, self.locator_dictionary['email'][1]).send_keys(user_name)
        improved_find_by(self.driver, self.locator_dictionary['password'][0], 10, self.locator_dictionary['password'][1]).send_keys(password)
        improved_find_by(self.driver, self.locator_dictionary['submit'][0], 10, self.locator_dictionary['submit'][1]).click()
        return MyAccount(self.driver)
