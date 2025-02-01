from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time,math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    browser.find_element(By.ID, "book").click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    x_num = browser.find_element(By.ID, "input_value")
    x = x_num.text
    y = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    
    browser.find_element(By.ID, "solve").click()
    
finally:
    time.sleep(10)
    browser.quit()