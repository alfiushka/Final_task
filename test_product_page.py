from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time


#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", \
#pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", \
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#def test_guest_can_add_product_to_basket(browser, link):
def test_guest_can_add_product_to_basket(browser):
   # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_in_basket() 
    #page.solve_quiz_and_get_code()
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()
    page.should_be_name_item()
    page.should_be_price_item()

def test_guest_should_see_login_link_on_product_page(browser):
   # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_in_basket() 
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_in_basket() 
    #page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_mini()
    page.go_to_basket_mini()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_empty()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage ():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_in_basket() 
        #page.solve_quiz_and_get_code()
        #login_page = LoginPage(browser, browser.current_url)
        #login_page.should_be_login_page()
        page.should_be_name_item()
        page.should_be_price_item()