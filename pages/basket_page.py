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
        print("should_not_be_order PASSED")
	
    def should_not_be_order(self):
        # Ожидаем, что в корзине нет товаров:
        assert self.is_not_element_present(*BasePageLocators.BOOK_IN_BASKET), \
            "Корзина не пуста, как ожидалось"
        print("BOOK_IN_BASKET == NULL PASSED")
        # Ожидаем, что есть текст о том, что корзина пуста: 
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), \
            "Нет сообщения о пустой корзине, как ожидалось"
        print("EMPTY_BASKET PASSED")
    
        