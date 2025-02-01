from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__)) 

try: 
    firstname = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    firstname.send_keys("Имя")
    
    lastname = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    lastname.send_keys("Фамилия")
    
    email = browser.find_element(By.CSS_SELECTOR,"[name = 'email']")
    email.send_keys("test@mail.test")
       
    file_path = os.path.join(current_dir, 'test.txt')
    attach = browser.find_element(By.ID, "file")
    attach.send_keys(file_path)
    
    submit = browser.find_element(By.CLASS_NAME,"btn").click()
    
    
finally:
    time.sleep(10)
    browser.quit()