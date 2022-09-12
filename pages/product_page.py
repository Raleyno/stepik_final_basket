from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.xfail
class ProductPage(BasePage):
    def add_to_basket(self):
        #self.should_not_be_success_message()        # test_guest_cant_see_success_message до заказа
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
    # название книги и ее цена:
        self.book = (self.browser.find_element(*ProductPageLocators.BOOK)).text
        self.price = (self.browser.find_element(*ProductPageLocators.PRICE)).text
        add_btn.click()
        self.solve_quiz_and_get_code()
    # название книги и ее цена в корзине:
        self.book_in_basket = (self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET)).text
        self.price_in_basket = (self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)).text
    # сравнить заказ и корзину:
    #    self.should_be_same_book()
    # Нет сообщения об успешном заказе:
    #    self.should_not_be_success_message()
	# Сообщение об успешном заказе исчезает:
    #    self.should_be_disappeared()
        
    def should_be_same_book(self):
        assert self.book == self.book_in_basket, "В корзине нет добавленного товара"
        assert self.price == self.price_in_basket, "Цена товара не совпадает с ценой добавленного товара"
    
    def should_not_be_success_message(self):
        #print("Успешно заказано" + self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
            
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    
        