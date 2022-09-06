from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return True
        return False
        
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
		
    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET)
        basket_btn.click()
                