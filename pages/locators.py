from selenium.webdriver.common.by import By
import pytest


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    INPUT_CONPASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "div.register_form button.btn.btn-lg.btn-primary")

class ProductPageLocators():
    ADD_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    #(By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_BOOK_INNER = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PPICE_BOOK = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_INNER = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_MINI = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PROCEED_CHECKOUT = (By.CSS_SELECTOR, "#btn-block")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
