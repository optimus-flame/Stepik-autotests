from selenium import webdriver
import time
import math
def calc(x):
    # Посчитать математическую функцию от x.
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link="http://suninjuly.github.io/redirect_accept.html"
    browser=webdriver.Chrome()
    browser.get(link)

# Отправляем заполненную форму
    button=browser.find_element_by_css_selector("button.btn")
    button.click()


    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn").click()


finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()