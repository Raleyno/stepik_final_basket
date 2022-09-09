from selenium.webdriver.common.by import By
import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import BasePageLocators
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time

class TestProductPage():
    # def __init__(self, browser, url):
    #    self.browser = browser
    #    self.url = url
    # test_guest_should_see_login_link_on_product_page(browser)    
    # test_guest_can_go_to_login_page_from_product_page(browser)    
    # test_guest_cant_see_product_in_basket_opened_from_product_page()    
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        time.sleep(1)
        page.should_be_login_link()    
        print("test_guest_should_see_login_link_on_product_page PASSED")
        
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, url)
        page.open()
        time.sleep(1)
        page.go_to_login_page() 
        print("test_guest_can_go_to_login_page_from_product_page PASSED")
        
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, url)
        page.open()
        page.go_to_basket()
        time.sleep(1)
        page.should_not_be_order()
        print("test_guest_cant_see_product_in_basket_opened_from_product_page PASSED")
        
# class TestUserAddToBasketFromProductPage():
    # def test_user_cant_see_success_message(browser)
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # page = ProductPage(browser, link)
        # page.open()
        # page.should_not_be_success_message()
        	
	# pytest -s -v test_main_page.py 	- запуск этого теста вызывается одноименной функцие из test_main_page.py 