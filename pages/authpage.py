from selenium.webdriver.common.by import By
from newclass import NewClass
import pages.myaccount


class AuthPage(NewClass):
    def __init__(self, driver):
        self.driver = driver

    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "submit": (By.ID, 'SubmitLogin')
    }

    def login(self, user_name, password):
        NewClass._find_by(self, *self.locator_dictionary['email']).send_keys(user_name)
        NewClass._find_by(self, *self.locator_dictionary['password']).send_keys(password)
        NewClass._find_by(self, *self.locator_dictionary['submit']).click()
        return pages.myaccount.MyAccount(self.driver)
