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

