from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "#login_form")
    reg_form = (By.CSS_SELECTOR, "#register_form")
    reg_email = (By.CSS_SELECTOR, "#id_registration-email")
    reg_password = (By.CSS_SELECTOR, "#id_registration-password1")
    confirm_password = (By.CSS_SELECTOR, "#id_registration-password2")
    reg_button = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a[href*="/basket/"]')
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
