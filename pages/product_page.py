from .base_page import BasePage
from .locators import ProductPageLocators
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
        assert product_name == message, "Name book not presented"

    def should_be_price_item(self):
        product_price = self.browser.find_element(*ProductPageLocators.PPICE_BOOK).text
        message_price = self.browser.find_element(*ProductPageLocators.PRICE_INNER).text
        print (product_price)
        assert product_price ==  message_price, "Price book not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_BOOK_INNER), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_BOOK_INNER), \
            "Success message is presented, but should not be"
            