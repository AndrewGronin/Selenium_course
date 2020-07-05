from selenium import webdriver
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(str(y))

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    rb = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script("window.scrollBy(0, 100);", rb)
    rb.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()