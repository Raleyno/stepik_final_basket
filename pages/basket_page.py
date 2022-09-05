from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
import time

class BasketPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.open()
        self.go_to_basket()
        time.sleep(1)
        self.should_not_be_order()
		
    def should_not_be_order(self):
        #print("Успешно заказано" + self.browser.find_element(*BasePageLocators.SUCCESS_MESSAGE).text)
        assert self.is_not_element_present(*BasePageLocators.BOOK_IN_BASKET), \
            "Корзина не пуста, как ожидалось"
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), \
            "Корзина не пуста, как ожидалось"
    
    
        