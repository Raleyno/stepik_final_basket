from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")             # Есть ссылка для входа/регистрации
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")         # Есть форма для входа
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")   # Есть форма регистрации
	
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")         # заказанная книга в корзине
    BASKET = (By.CSS_SELECTOR, "a[href$='/basket/'")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div #content_inner")