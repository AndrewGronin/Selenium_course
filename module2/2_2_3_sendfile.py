from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    in1 = browser.find_element_by_css_selector('[name="firstname"]')
    in2 = browser.find_element_by_css_selector('[name="lastname"]')
    in3 = browser.find_element_by_css_selector('[name="email"]')

    in1.send_keys("1")
    in2.send_keys("1")
    in3.send_keys("1")

    file = browser.find_element_by_css_selector('#file')

    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла

    file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()