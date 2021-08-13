from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Cant find word login in url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_adress = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS)
        email_adress.send_keys(email)
        password_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_1)
        password_1.send_keys(password)
        password_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
        password_2.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()
