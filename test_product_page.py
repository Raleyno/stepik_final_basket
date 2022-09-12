from selenium.webdriver.common.by import By
import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time

@pytest.mark.need_review
class TestProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link()    
        print("test_guest_should_see_login_link_on_product_page PASSED")
        
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, url)
        page.open()
        page.go_to_login_page() 
        print("test_guest_can_go_to_login_page_from_product_page PASSED")
        
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, url)
        page.open()
        page.go_to_basket()
        page.should_not_be_order()
        print("test_guest_cant_see_product_in_basket_opened_from_product_page PASSED")

@pytest.mark.register
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + '@fakemail.org'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, "Passw#200")	 # регистрация нового юзера
        page.should_be_authorized_user()             # регистрация/авторизация прошла успешно?

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        print("test_user_cant_see_success_message_opened_from_product_page PASSED")
            
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()            	# регистрация/авторизация прошла успешно?
        page.add_to_basket()
        print("test_user_can_add_product_to_basket_opened_from_product_page PASSED")
		
class TestGuestAddToBasketFromProductPage():
    @pytest.mark.xfail									# Тест ожидаемо должен упасть - товар добавлен
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        print("test_guest_cant_see_success_message_opened_from_product_page PASSED")
    
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        print("test_guest_can_add_product_to_basket_opened_from_product_page PASSED")

		# pytest -s -v test_product_page.py 	- запуск этого теста 