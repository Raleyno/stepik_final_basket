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
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")       # кнопка добавить в корзину
    BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")            # название книги
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")         # заказанная книга в корзине
    PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")         # цена книги       
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")      # цена заказанной книги в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")               # успешно добавлено в корзину 