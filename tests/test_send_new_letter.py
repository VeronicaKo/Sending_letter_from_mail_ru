from pages.MailPages import AddLetterPage

import config


def test_add_letter(login_as_user, browser):
    letter_page = AddLetterPage(browser)
    letter_page.go_to_letter_site()
    letter_page.enter_email(config.recipient)
    letter_page.enter_subject('English proverbs')
    letter_page.enter_text_of_letter(
        'A cat in gloves catches no mice. Many hands make light work. An apple a day keeps the doctor away.')
    letter_page.click_on_the_button_send()
    assert letter_page.checking_sending_letter(), "The email has not been sent"
