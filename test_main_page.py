from pages.basket_page import BasketPage
from selenium.webdriver.common.by import By

#def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = BasketPage(browser, link)
	page.open()
	
		
	# pytest -s -v test_main_page.py 	- запуск