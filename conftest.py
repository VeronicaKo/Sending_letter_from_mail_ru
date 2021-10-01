import pytest
from selenium import webdriver
from pages.MailPages import LogInPage
import config
from pages.LetterPage import AddLetterPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_as_user(browser):
    login_as_user = LogInPage(browser)
    login_as_user.go_to_site()
    login_as_user.enter_login(config.login)
    login_as_user.enter_domain(config.domain)
    login_as_user.click_on_the_password_button()
    login_as_user.enter_password(config.password)
    login_as_user.click_on_the_enter_button()
    return AddLetterPage(browser)
