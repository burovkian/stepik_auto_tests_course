from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_num = browser.find_element(By.ID, "input_value")
    x = x_num.text
    y = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()