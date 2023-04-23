from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(2)


    try:
        button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').is_displayed()
        assert button is not None,"Button found!"
       # print('Button found!')

    except:
        print('Button NOT found!')

    