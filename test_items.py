link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.get(link)

    #find the button
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), 'Choose another language'
