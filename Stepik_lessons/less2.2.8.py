import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/file_input.html"

try: 
    
    browser = webdriver.Chrome()
    browser.get(link) 
    
    text1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    text1.send_keys("TEST")
    text2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    text2.send_keys("TESTOV")
    text3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    text3.send_keys("TEST@bk.ru")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "attach.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла