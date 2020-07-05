from selenium import  webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    firstName = browser.find_element_by_css_selector(".first:required")
    firstName.send_keys("Ivan")
    lastName = browser.find_element_by_css_selector(".second:required")
    lastName.send_keys("Petrov")
    email = browser.find_element_by_css_selector(".third:required")
    email.send_keys("mail@test.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_elt = browser.find_element_by_tag_name("h1")

    # записываем в переменную welcome_text текст из элемента welcome_elt
    welcome_text = welcome_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
