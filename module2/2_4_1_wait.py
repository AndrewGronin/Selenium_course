import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    b = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price'),"$100")
    )
    button = browser.find_element_by_css_selector('button')
    button.click()



    xel = browser.find_element_by_css_selector('#input_value')
    x = xel.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    ans = calc(int(x))

    in1 = browser.find_element_by_css_selector('#answer')
    in1.send_keys(str(ans))

    sub = browser.find_element_by_css_selector('#solve')
    sub.click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()