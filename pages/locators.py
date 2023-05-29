from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

# class MainPageLocators():
#     LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ItemPageLocators():
    ADD_CART_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

