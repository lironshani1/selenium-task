from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NewClass(object):

    def __init__(self, driver):
        self.driver = driver

    def _find_by(self, find_by, param, seconds_to_wait=10):

        elem_to_return = WebDriverWait(self.driver, seconds_to_wait).until(ec.visibility_of_element_located((find_by, param)))

        return elem_to_return
