from selenium.webdriver.common.by import By
import pytest


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    #(By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_BOOK_INNER = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PPICE_BOOK = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_INNER = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
