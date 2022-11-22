import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('sublink', ['employees/', 'novostroyki/', '', 'sale/apartments/', 'rent/apartments/', ])
def test_guest_should_see_login_link(browser, sublink):
    link = f"https://anflat.ru/{sublink}"
    browser.get(link)
    browser.refresh()
