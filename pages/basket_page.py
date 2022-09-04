from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def go_to_basket(self):
        #self.should_not_be_success_message()        # test_guest_cant_see_success_message до заказа
        #basket_btn = self.browser.find_element(*BasePageLocators.BASKET)
		#basket_btn.click()
        self.should_not_be_order()
		
    def should_not_be_order(self):
        #print("Успешно заказано" + self.browser.find_element(*BasePageLocators.SUCCESS_MESSAGE).text)
        assert self.is_not_element_present(*ProductPageLocators.EMPTY_BASKET), \
            "Success message is presented, but should not be"
    
    
    
        