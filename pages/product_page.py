from .base_page import BasePage
from .locators import ProductPageLocators
#from .login_page import LoginPage
#from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage): 
    def go_in_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket.click()
    def should_be_name_item(self):
        time.sleep(3)
        product_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        message = self.browser.find_element(*ProductPageLocators.NAME_BOOK_INNER).text
        print (product_name)
        print (message)
        #assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert product_name == message, "Name book not presented"

    def should_be_price_item(self):
        product_price = self.browser.find_element(*ProductPageLocators.PPICE_BOOK).text
        message_price = self.browser.find_element(*ProductPageLocators.PRICE_INNER).text
        print (product_price)
        assert product_price ==  message_price, "Price book not presented"