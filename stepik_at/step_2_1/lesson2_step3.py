from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time,math

def calc(x1,x2):
    return str(int(x1)+int(x2))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID,"num1")  
    x_num1 = num1.text
    
    num2 = browser.find_element(By.ID,"num2")
    x_num2 = num2.text
    
    sum = calc(x_num1,x_num2)
    
    open_list = Select(browser.find_element(By.ID, "dropdown"))
    open_list.select_by_value(sum)
    
    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()
    
finally:
    time.sleep(5)
    browser.quit()