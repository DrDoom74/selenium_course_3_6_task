import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    bttn = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert bttn, "no button for adding basket found"