import pytest
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities
import os
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="function", autouse=True)
def get_driver():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    time.sleep(1)
    yield driver
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=d)
    driver.quit()


def improved_find_by(driver, find_by, seconds_to_wait=10, param=None):
    try:
        elem_to_return = WebDriverWait(driver, seconds_to_wait).until(ec.visibility_of_element_located((find_by, param)))
    except Exception as e:
        raise e
    # color_change = f"arguments[0].setAttribute('style', 'background-color:red;')"
    # driver.execute_script(color_change, elem_to_return)
    return elem_to_return