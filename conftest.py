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
    login_page = LogInPage(browser)
    login_page.go_to_site()
    login_page.enter_login(config.login)
    login_page.enter_domain(config.domain)
    login_page.click_on_the_password_button()
    login_page.enter_password(config.password)
    login_page.click_on_the_enter_button()
    assert login_page.checking_move_on_letter_page(), 'The login to the email is not completed'
    return AddLetterPage(browser)
