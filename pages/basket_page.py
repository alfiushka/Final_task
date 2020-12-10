from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage): 
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_CHECKOUT), \
            "Items is presented in basket, but should not be"
    def should_be_basket_empty(self):
        message_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        print (message_empty)
        assert message_empty == "Your basket is empty. Continue shopping", "Your basket is empty not presented" 
        