from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os
from math import *

driver = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд


driver.get("http://suninjuly.github.io/explicit_wait2.html")
button = driver.find_element(By.ID, "book")
indicator = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()
x_element_ebuchiy = driver.find_element(By.ID, "input_value")
x = x_element_ebuchiy.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
answer = driver.find_element(By.ID, "answer")
answer.send_keys(y)
submit = driver.find_element(By.ID, "solve")
submit.click()
