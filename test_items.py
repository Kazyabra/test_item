# запуск теста из консоли: pytest -s --language=es test_items.py
import pytest
from selenium.webdriver.common.by import By


def test_find_button_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(5)
    button = None
    error = 'BUTTON "Add to basket" NOT FOUND'
    try:
        browser.get(link)
    except:
        error = 'LINK NOT FOUND'
    try:
        button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    finally:
        assert button is not None, error


if __name__ == '__main__':
    pytest.main()
