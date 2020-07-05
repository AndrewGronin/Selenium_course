import math

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    b1 = browser.find_element_by_css_selector('button')
    b1.click()

    alert = browser.switch_to.alert
    alert.accept()

    xel = browser.find_element_by_css_selector('#input_value')
    x = xel.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    ans = calc(int(x))

    in1 = browser.find_element_by_css_selector('#answer')
    in1.send_keys(str(ans))

    sub = browser.find_element_by_css_selector('button')
    sub.click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()