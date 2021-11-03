import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


def pytest_addoption(parser):
    # добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    # добавляем параметр запуска тестов в командной строке(указание языка запуска вебдрайвера) По умолчанию "ru"
    parser.addoption('--language', action='store', default="ru", help="Choose you language")


# Запуск браузера(для каждой функции)
# Запуск тестов на Firefox:
# pytest -s -v --browser_name=firefox --language=ru test_parser.py
# Запуск тестов на Chrome:
# pytest -s -v --browser_name=chrome --language=ru test_parser.py
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    # получаем параметр командной строки language
    user_language = request.config.getoption("language")
    # получаем параметр командной строки browser_name
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        # Задаем в опциях браузера language, который получили из командной строки
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # запускаем браузер
        browser = webdriver.Chrome(options=options)
        print("\nstart Сhrome browser for test..")
    elif browser_name == "firefox":
        # Задаем в опциях браузера language, который получили из командной строки
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        # запускаем браузер
        browser = webdriver.Firefox(firefox_profile=fp)
        print("\nstart Firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
