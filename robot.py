import math
from selenium import webdriver
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    a=browser.find_element_by_id("input_value").text
    y = calc(a)
    field = browser.find_element_by_id("answer")
    field.send_keys(y)
    option1=browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2=browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    
    