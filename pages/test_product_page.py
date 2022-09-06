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
        self.test_guest_should_see_login_link_on_product_page(browser)
        print("test_guest_should_see_login_link_on_product_page PASSED")
        self.test_guest_can_go_to_login_page_from_product_page(browser)
        print("test_guest_can_go_to_login_page_from_product_page PASSED")
        self.test_guest_cant_see_product_in_basket_opened_from_product_page()
        print("test_guest_cant_see_product_in_basket_opened_from_product_page PASSED")
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        
        #page = BasePage(browser, url)
        self.open()
        time.sleep(1)
        self.should_be_login_link()    
    
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        #url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        #page = BasePage(browser, url)
        self.open()
        time.sleep(1)
        self.go_to_login_page() 
        
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        page = BasketPage(self.browser, self.url)
        page.open()
        page.go_to_basket()
        time.sleep(1)
        page.should_not_be_order()
        	
	# pytest -s -v test_main_page.py 	- запуск этого теста вызывается одноименной функцие из test_main_page.py 