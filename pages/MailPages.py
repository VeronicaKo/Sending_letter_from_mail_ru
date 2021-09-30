from pages.baseApp import BasePage

from selenium.webdriver.common.by import By


class MailLocators:
    LOCATOR_MAIL_LOGIN = (By.CSS_SELECTOR, 'input[data-testid="login-input"]')
    LOCATOR_MAIL_DOMAIN = (By.NAME, 'domain')
    LOCATOR_BUTTON_INPUT_PASSWORD = (By.CSS_SELECTOR, 'button[data-testid="enter-password"]')
    LOCATOR_MAIL_PASSWORD = (By.CSS_SELECTOR, 'input[data-testid="password-input"]')
    LOCATOR_BUTTON_ENTER = (By.CSS_SELECTOR, 'button[data-testid="login-to-mail"]')
    LOCATOR_MESSAGE_ABOUT_WRONG_PASSWORD = (By.CLASS_NAME, 'error.svelte-1tib0qz')

    LOCATOR_BUTTON_NEW_LETTER = (By.CSS_SELECTOR, '[title="Написать письмо"]')
    LOCATOR_ENTER_EMAIL = (By.CSS_SELECTOR, 'input.container--H9L5q.size_s_compressed--2c-eV')
    LOCATOR_ENTER_SUBJECT = (By.CSS_SELECTOR, 'input[name="Subject"]')
    LOCATOR_ENTER_TEXT_OF_LETTER = (By.CSS_SELECTOR, ".cke_editable_inline.cke_contents_true.cke_show_borders>div")
    LOCATOR_CLICK_ON_THE_BUTTON_SEND = (By.CSS_SELECTOR, '.button2_primary>span>span')
    LOCATOR_MESSAGE_ABOUT_SUCCESS_SENDING = (By.CLASS_NAME, "layer__link")


class LogIn(BasePage):
    def enter_login(self, email_name: str):
        login_field = self.find_element(MailLocators.LOCATOR_MAIL_LOGIN)
        login_field.click()
        login_field.send_keys(email_name)

    def enter_domain(self, domain_name: str):
        domain_field = self.find_element(MailLocators.LOCATOR_MAIL_DOMAIN)
        domain_field.click()
        domain_field.send_keys(domain_name)

    def click_on_the_password_button(self):
        self.find_element(MailLocators.LOCATOR_BUTTON_INPUT_PASSWORD, time=2).click()

    def enter_password(self, pass_name: str):
        pass_field = self.find_element(MailLocators.LOCATOR_MAIL_PASSWORD)
        pass_field.click()
        pass_field.send_keys(pass_name)

    def click_on_the_enter_button(self):
        self.find_element(MailLocators.LOCATOR_BUTTON_ENTER, time=2).click()

    def message_about_wrong_password_login(self):
        self.is_element_present(MailLocators.LOCATOR_MESSAGE_ABOUT_WRONG_PASSWORD)

    def checking_move_on_letter_page(self):
        return self.is_element_present(MailLocators.LOCATOR_BUTTON_NEW_LETTER)


class AddLetter(BasePage):

    def enter_email(self, email: str):
        email_field = self.find_element(MailLocators.LOCATOR_ENTER_EMAIL)
        email_field.click()
        email_field.send_keys(email)

    def enter_subject(self, subject: str):
        subject_field = self.find_element(MailLocators.LOCATOR_ENTER_SUBJECT)
        subject_field.click()
        subject_field.send_keys(subject)

    def enter_text_of_letter(self, text: str):
        text_field = self.find_element(MailLocators.LOCATOR_ENTER_TEXT_OF_LETTER)
        text_field.click()
        text_field.send_keys(text)

    def click_on_the_button_send(self):
        self.find_element(MailLocators.LOCATOR_CLICK_ON_THE_BUTTON_SEND, time=2).click()

    def checking_sending_letter(self):
        return self.is_element_present(MailLocators.LOCATOR_BUTTON_NEW_LETTER)
