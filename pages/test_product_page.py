from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import pytest
from .base_page import BasePage
from .locators import LoginPageLocators

class ProductPage(BasePage):
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_order()
		page.go_to_basket()
	# pytest -s -v test_product_page.py 	- запуск этого теста