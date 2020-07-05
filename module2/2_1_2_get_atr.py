from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(str(y))

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    rb = browser.find_element_by_css_selector('#robotsRule')
    rb.click()

    submit = browser.find_element_by_css_selector('.btn')
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()