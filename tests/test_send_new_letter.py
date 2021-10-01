import config
from pages.MailPages import LogInPage


def test_log_in(browser):
    current_page = LogInPage(browser)
    current_page.go_to_site()
    current_page.enter_login(config.login)
    current_page.enter_domain(config.domain)
    current_page.click_on_the_password_button()
    current_page.enter_password(config.password)
    current_page.click_on_the_enter_button()
    assert current_page.checking_move_on_letter_page(), 'The login to the email is not completed'


def test_add_letter(login_as_user):
    login_as_user.go_to_letter_site()
    login_as_user.enter_email(config.recipient)
    login_as_user.enter_subject('English proverbs')
    login_as_user.enter_text_of_letter(
        'A cat in gloves catches no mice. Many hands make light work. An apple a day keeps the doctor away.')
    login_as_user.click_on_the_button_send()
    assert login_as_user.checking_sending_letter(), "The email has not been sent"
