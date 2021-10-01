from time import sleep

import pytest
from selenium import webdriver
from pages.MailPages import LogInPage
import config


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    sleep(10)
    driver.quit()


@pytest.fixture(scope="session")
def login_as_user(browser):
    login_as_user = LogInPage(browser)
    login_as_user.go_to_site()
    login_as_user.enter_login(config.login)
    login_as_user.enter_domain(config.domain)
    login_as_user.click_on_the_password_button()
    login_as_user.enter_password(config.password)
    login_as_user.click_on_the_enter_button()
    assert login_as_user.checking_move_on_letter_page(), 'The login to the email is not completed'
