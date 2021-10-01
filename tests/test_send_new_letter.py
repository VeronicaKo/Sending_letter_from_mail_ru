from pages.MailPages import AddLetterPage
from pages.MailPages import LogInPage

import config


def test_log_in(browser):
    current_page = LogInPage(browser)
    current_page.go_to_site()
    current_page.enter_login(config.login)
    current_page.enter_domain(config.domain)
    current_page.click_on_the_password_button()
    current_page.enter_password(config.password)
    current_page.click_on_the_enter_button()
    assert current_page.checking_move_on_letter_page(), 'The login to the email is not completed'


def test_add_letter(browser):
    current_page = LogInPage(browser)
    current_page.go_to_site()
    current_page.enter_login(config.login)
    current_page.enter_domain(config.domain)
    current_page.click_on_the_password_button()
    current_page.enter_password(config.password)
    current_page.click_on_the_enter_button()
    assert current_page.checking_move_on_letter_page(), 'The login to the email is not completed'

    letter_page = AddLetterPage(browser)
    letter_page.go_to_letter_site()
    letter_page.enter_email(config.recipient)
    letter_page.enter_subject('English proverbs')
    letter_page.enter_text_of_letter(
        'A cat in gloves catches no mice. Many hands make light work. An apple a day keeps the doctor away.')
    letter_page.click_on_the_button_send()
    assert letter_page.checking_sending_letter(), "The email has not been sent"
