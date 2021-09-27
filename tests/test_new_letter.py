import pytest

from pages.MailPages import AddLetter
from pages.MailPages import LogIn


def test_log_in(browser):
    current_page = LogIn(browser)
    current_page.go_to_site()
    current_page.enter_login("abvera")
    current_page.enter_domain("@list.ru")
    current_page.click_on_the_password_button()
    current_page.enter_password("123")
    current_page.click_on_the_enter_button()

    print(111, current_page.message_about_wrong_password_login)
    assert current_page.message_about_wrong_password_login == 'Неверное имя или пароль', 'The entrance to email is not completed'


def add_letter(browser):
    search_page = AddLetter(browser)


    #
    # search_page.go_to_site()
    # search_page.click_on_the_search_button()
    # search_page.enter_word("shirt")
    # search_page.click_on_the_search_button_start()
    assert 2 == 1+1
    # elements = search_page.check_navigation_bar()
    # assert "Картинки" and "Видео" in elementsd_be_login_link()


if __name__ == '__main__':
    pytest.main()




