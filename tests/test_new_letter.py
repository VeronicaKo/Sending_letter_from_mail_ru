import pytest

from pages.MailPages import AddLetter
from pages.MailPages import LogIn


def test_log_in(browser):
    current_page = LogIn(browser)
    current_page.go_to_site()
    current_page.enter_login("abvera")
    current_page.enter_domain("@list.ru")
    current_page.click_on_the_password_button()
    current_page.enter_password("rehm`3ysq")
    current_page.click_on_the_enter_button()
    assert current_page.checking_move_on_letter_page() == False, 'The login to the email is not completed'


def test_add_letter(browser):
    letter_page = AddLetter(browser)
    letter_page.go_to_letter_site()
    # letter_page.click_on_the_button_new_letter()
    letter_page.enter_email('ask@quality-lab.ru')
    letter_page.enter_subject('Задание Кошелевой Веры')
    letter_page.enter_text_of_letter(
        f'Здравствуйте, высылаю вам моё тестовое задание по тестированию https://github.com/VeronicaKo/quality_lab.git')
    letter_page.click_on_the_button_send()

    #
    # search_page.go_to_site()
    # search_page.click_on_the_search_button()
    # search_page.enter_word("shirt")
    # search_page.click_on_the_search_button_start()
    assert 2 == 1 + 1
    # elements = search_page.check_navigation_bar()
    # assert "Картинки" and "Видео" in elementsd_be_login_link()

    if __name__ == '__main__':
        pytest.main()
