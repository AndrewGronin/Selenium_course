from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_el = browser.find_element_by_css_selector('#num1')
    x2_el = browser.find_element_by_css_selector('#num2')

    x1 = x1_el.text
    x2 = x2_el.text

    res = int(x1)+int(x2)


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(res))

    submit = browser.find_element_by_css_selector('.btn')
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()