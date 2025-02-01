from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox1.click()
    
    radio1 = browser.find_element(By.CSS_SELECTOR, "[type='radio'][value='robots']")
    radio1.click()
    
    submit1 = browser.find_element(By.CLASS_NAME, 'btn')
    submit1.click()
    
finally:
    time.sleep(5)
    browser.quit()