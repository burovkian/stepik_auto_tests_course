from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    num_x = browser.find_element(By.ID, "input_value")
    x = num_x.text
    y = calc(x)

    value_field = browser.find_element(By.ID, "answer")
    value_field.send_keys(y)
    
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    
    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    

    
    radio = browser.find_element(By.CSS_SELECTOR, "[type='radio'][value = 'robots']")
    radio.click()

    button.click()
    
finally:
    time.sleep(5)
    browser.quit()