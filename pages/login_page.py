from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver
import time

class LoginPage(BasePage):
            
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url,  f"expected 'login' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "отсутствует форма для входа"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "отсутствует форма для регистрации"
        
    def register_new_user(self, email, password):
        # Регистрация нового рандомного пользователя:
        mail = self.browser.find_element(*LoginPageLocators.MAIL)
        mail.send_keys(email)
        passw = self.browser.find_element(*LoginPageLocators.PASSW)
        passw2 = self.browser.find_element(*LoginPageLocators.PASSW2)
        passw.send_keys(password)
        passw2.send_keys(password)
        submit_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        submit_btn.click()
        time.sleep(5)
        