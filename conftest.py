import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default= "chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose language: es, ru or fr and ...")

#options = Options()
#options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#browser = webdriver.Chrome(options=options)

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    #browser = None
    if browser_name == "chrome":
        options = Options() 
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) 
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile() 
        fp.set_preference("intl.accept_languages", user_language) 
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--language_name should be ")
    yield browser
    print("\nquit browser..")
    browser.quit()