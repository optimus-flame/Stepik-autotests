from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html?"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_css_selector("[id="num1"]").get.attribute("text")
    num2 = browser.find_element_by_css_selector("[id="num2"]").get.attribute("text")
    s= num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s) # ищем элемент с текстом "Python"
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    