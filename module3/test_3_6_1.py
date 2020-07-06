import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getAns():
    return str(math.log(int(time.time())))



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                    'https://stepik.org/lesson/236896/step/1',
                                    'https://stepik.org/lesson/236897/step/1',
                                    'https://stepik.org/lesson/236898/step/1',
                                    'https://stepik.org/lesson/236899/step/1',
                                    'https://stepik.org/lesson/236903/step/1',
                                    'https://stepik.org/lesson/236904/step/1',
                                    'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):

    browser.get(link)

    b = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.string-quiz__textarea'))
    )
    #time.sleep(10)

    in1 = browser.find_element_by_css_selector(".string-quiz__textarea")
    in1.click()
    in1.send_keys(getAns())
    sub = browser.find_element_by_css_selector(".submit-submission")
    sub.click()
    time.sleep(5)
    assert True