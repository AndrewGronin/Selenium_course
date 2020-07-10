import time



def test_is_basket_button_present(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_bask = browser.find_element_by_css_selector(".btn-add-to-basket")

    time.sleep(5)

    assert add_to_bask, "button not found"