from pages.basket_page import BasketPage
from pages.test_product_page import ProductPage
from selenium.webdriver.common.by import By

#def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com"
    url2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208"
    page = BasketPage(browser, url)
    page2 = ProductPage(browser, url2)
    
	# pytest -s -v test_main_page.py 	- запуск