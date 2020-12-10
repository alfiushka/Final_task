from .base_page import BasePage
from .locators import LoginPageLocators
import time
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login not presented in this link" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form  is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        inputemail = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        inputemail.send_keys(email)
        inputpassword = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        inputpassword.send_keys("Password123!")
        inputconpassword = self.browser.find_element(*LoginPageLocators.INPUT_CONPASSWORD)
        inputconpassword.send_keys("Password123!")
        buttonreg = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        buttonreg.click()
        
