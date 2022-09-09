from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from test_product_page import ProductPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url  
        page.open()                       # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        print("test_guest_can_go_to_login_page PASSED")
                    
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()
        print("test_guest_should_see_login_link PASSED")    
        # pytest -v --tb=line --language=en test_main_page.py 	- запуск
    
    # pytest -s -v -m login_guest   - запуск только этих 2 тестов с маркировкой- @pytest.mark.login_guest
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, url)
    print("test_guest_cant_see_product_in_basket_opened_from_main_page PASSED")

	# pytest -s -v test_main_page.py 	- запуск