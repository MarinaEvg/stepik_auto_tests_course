from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/selects1.html"

try: 
    
    browser = webdriver.Chrome()
    browser.get(link) 
   
    a = browser.find_element(By.ID, "num1")
    x=int(a.text)
    b = browser.find_element(By.ID, "num2")
    y=int(b.text)
    sum=x+y
    
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла