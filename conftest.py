from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    sleep(10)
    driver.quit()


