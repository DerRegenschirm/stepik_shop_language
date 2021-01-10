import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")

    language = request.config.getoption("language")

    # languages for Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()