from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class MailLocators:
    LOCATOR_MAIL_LOGIN = (By.CSS_SELECTOR, 'input[data-testid="login-input"]')
    LOCATOR_MAIL_DOMAIN = (By.NAME, 'domain')
    LOCATOR_BUTTON_INPUT_PASSWORD = (By.CSS_SELECTOR, 'button[data-testid="enter-password"]')
    LOCATOR_MAIL_PASSWORD = (By.CSS_SELECTOR, 'input[data-testid="password-input"]')
    LOCATOR_BUTTON_ENTER = (By.CSS_SELECTOR, 'button[data-testid="login-to-mail"]')
    LOCATOR_MESSAGE_ABOUT_WRONG_PASSWORD = (By.CLASS_NAME, 'error.svelte-1tib0qz')
    LOCATOR_BUTTON_NEW_LETTER = (By.CSS_SELECTOR, '[title="Написать письмо"]')


class LogInPage(BasePage):
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
