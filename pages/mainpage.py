from newclass import NewClass
from pages.authpage import AuthPage
from selenium.webdriver.common.by import By
from pages.searchresult import SearchResult


class MainPage(NewClass):
    def __init__(self, driver):
        self.driver = driver

    locator_dictionary = {
        "login": (By.CLASS_NAME, 'login'),
        "search": (By.ID, "search_query_top"),
        "btn_search": (By.CLASS_NAME, "button-search")
    }

    def sign_in(self):
        NewClass._find_by(self, *self.locator_dictionary['login']).click()
        return AuthPage(self.driver)

    def search(self, search_value):
        NewClass._find_by(self, *self.locator_dictionary['search']).send_keys(search_value)
        NewClass._find_by(self, *self.locator_dictionary['btn_search']).click()
        return SearchResult

