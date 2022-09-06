from selenium.webdriver.common.by import By

    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")         # Есть форма для входа
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")   # Есть форма регистрации
	
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")                   # Есть ссылка для входа/регистрации
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")       # Несуществующая ссылка
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")     # Заказанная книга в корзине
    BASKET = (By.CSS_SELECTOR, "a[href$='/basket/'")                # Ссылка на корзину
    EMPTY_BASKET = (By.CSS_SELECTOR, "div #content_inner")          # Признак пустой корзины