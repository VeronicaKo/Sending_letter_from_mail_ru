
from pages.baseApp import BasePage

from selenium.webdriver.common.by import By


class MailLocators:
    LOCATOR_MAIL_LOGIN = (By.CSS_SELECTOR, 'input[data-testid="login-input"]')
    LOCATOR_MAIL_DOMAIN = (By.NAME, 'domain')
    LOCATOR_BUTTON_INPUT_PASSWORD = (By.CSS_SELECTOR, 'button[data-testid="enter-password"]')
    LOCATOR_MAIL_PASSWORD = (By.CSS_SELECTOR, 'input[data-testid="password-input"]')
    LOCATOR_BUTTON_ENTER = (By.CSS_SELECTOR, 'button[data-testid="login-to-mail"]')
    LOCATOR_MESSAGE_ABOUT_WRONG_PASSWORD = (By.CLASS_NAME, 'error.svelte-1tib0qz')

class LogIn(BasePage):
    def enter_login(self, emailName: str):
        login_field = self.find_element(MailLocators.LOCATOR_MAIL_LOGIN)
        login_field.click()
        login_field.send_keys(emailName)
        return login_field

    def enter_domain(self, domainName: str):
        domain_field = self.find_element(MailLocators.LOCATOR_MAIL_DOMAIN)
        domain_field.click()
        domain_field.send_keys(domainName)
        return domain_field

    def click_on_the_password_button(self):
        return self.find_element(MailLocators.LOCATOR_BUTTON_INPUT_PASSWORD, time=2).click()

    def enter_password(self, passName: str):
        pass_field = self.find_element(MailLocators.LOCATOR_MAIL_PASSWORD)
        pass_field.click()
        pass_field.send_keys(passName)
        return pass_field

    def click_on_the_enter_button(self):
        return self.find_element(MailLocators.LOCATOR_BUTTON_ENTER, time=2).click()

    def message_about_wrong_password_login(self):
        return self.find_element(MailLocators.LOCATOR_MESSAGE_ABOUT_WRONG_PASSWORD)


class AddLetter(BasePage):
    def click_on_the_search_button(self):
        return self.find_element(MailLocators.BUTTON_SEARCH, time=2).click()
    #
    # def enter_word(self, word: str):
    #     search_field = self.find_element(MailLocators.INPUT_KEY_WORD)
    #     search_field.click()
    #     search_field.send_keys(word)
    #     return search_field
    #
    # def click_on_the_search_button_start(self):
    #     return self.find_element(MailLocators.BUTTON_SEARCH_START, time=2).click()
    #
    # def product_found(self):
    #     self.find_element(MailLocators.PRODUCTS_TITLES)
    #
    # def message_product_not_found(self):
    #     self.find_element(MailLocators.MESSAGE_PRODUCT_NOT_FOUND)
    #
    # def enter_price_ot(self, price: int):
    #     search_field = self.find_element(MailLocators.INPUT_OT)
    #     search_field.click()
    #     search_field.send_keys(price)
    #     return search_field
    #
    # def enter_price_do(self, price: int):
    #     search_field = self.find_element(MailLocators.INPUT_DO)
    #     search_field.click()
    #     search_field.send_keys(price)
    #     return search_field
