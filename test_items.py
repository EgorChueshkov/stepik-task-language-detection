from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time


def check_exist_button(browser):
    try:
        browser.find_element_by_css_selector('#add_to_basket_form > button')
    except NoSuchElementException:
        return False
    return True


def test_check_exist_element(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    assert check_exist_button(browser), 'element not found'

