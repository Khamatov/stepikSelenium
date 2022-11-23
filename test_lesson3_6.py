import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()
#, "236896", "236897", "236898", "236899", "236903", "236904", "236905"
@pytest.mark.parametrize("sublink",["236895"])
def test_for_men_part_one(browser, sublink):
    link = f"https://stepik.org/lesson/{sublink}/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click() ## click for "to come in" button
    browser.find_element(By.NAME, "login").send_keys('')
    browser.find_element(By.NAME, "password").send_keys('')
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()