from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_num = browser.find_element(By.ID, "input_value")
    x = x_num.text
    y = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()