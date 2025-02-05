import time,math,pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = ""
pas = ""

url_list = ["236895","236896","236897","236898","236899","236903","236904","236905"]

def math_part():
    return (math.log(int(time.time())))

@pytest.mark.parametrize('url_part',url_list)
def test_auth_stepik(browser,url_part):
    link = f"https://stepik.org/lesson/{url_part}/step/1"
    browser.get(link)
    browser.implicitly_wait(20)
    browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    browser.find_element(By.CSS_SELECTOR,"[name='login']").send_keys(log)
    browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(pas)
    button1 = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"[type='submit']"))
    )
    button1.click()
    time.sleep(5)
    text_area = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.TAG_NAME,"textarea"))
    )
        #(browser.find_element(By.TAG_NAME,"textarea"))
    text_area.send_keys(math_part())

    button2 = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"[class='submit-submission']"))
    )
    button2.click()

    #button2 = browser.find_element(By.CSS_SELECTOR,"[class='submit-submission']")
    #button2.click()
    correct_check = browser.find_element(By.CSS_SELECTOR,"[class='smart-hints__hint']").text
    #correct_check = WebDriverWait(browser, 12).until(
     #       EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class='smart-hints__hint']"),"Correct!")
     #   )

    assert correct_check == "Correct!", f"DONE!"
    time.sleep(1)
    #text_to_be_present_in_element







