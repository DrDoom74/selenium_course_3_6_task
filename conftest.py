import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):  # обработчик опции language
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")  # забираем значение language
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # выбор языка
    if user_language == "es":
        print("\nstart browser for test with es as pref lang..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "fr":
        print("\nstart browser for test with fr as pref lang..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--Pref language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()