from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from math import *
from selenium.webdriver.support.ui import Select
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()
    second_page = driver.window_handles[1]
    driver.switch_to.window(second_page)
    time.sleep(0.5)
    x_element_ebuchiy = driver.find_element(By.ID, "input_value")
    x = x_element_ebuchiy.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # print(answer)