from pages.authpage import AuthPage
from selenium.webdriver.common.by import By
from conftest import improved_find_by
from pages.searchresult import SearchResult


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    locator_dictionary = {
        "login": (By.CLASS_NAME, 'login'),
        "search": (By.ID, "search_query_top"),
        "btn_search": (By.CLASS_NAME, "button-search")
    }

    def sign_in(self):
        improved_find_by(self.driver, self.locator_dictionary['login'][0], 10, self.locator_dictionary['login'][1]).click()
        return AuthPage(self.driver)

    def search(self, search_value):
        improved_find_by(self.driver, self.locator_dictionary['search'][0], 10, self.locator_dictionary['search'][1]).send_keys(search_value)
        improved_find_by(self.driver, self.locator_dictionary['btn_search'][0], 10, self.locator_dictionary['btn_search'][1]).click()
        return SearchResult

