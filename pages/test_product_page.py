from selenium.webdriver.common.by import By
import pytest
from .base_page import BasePage
from .basket_page import BasketPage
from .locators import BasePageLocators
import time

class ProductPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.test_guest_cant_see_product_in_basket_opened_from_product_page()
        
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        page = BasketPage(self.browser, self.url)
        page.open()
        page.go_to_basket()
        time.sleep(1)
        page.should_not_be_order()
		
	# pytest -s -v test_product_page.py 	- запуск этого теста