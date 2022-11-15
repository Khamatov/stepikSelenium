from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link)
    firstname = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    firstname.send_keys('Azatello')
    lastname = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    lastname.send_keys('Hamatello')
    email = driver.find_element(By.CSS_SELECTOR, ".form-control.third")
    email.send_keys("azat@mail.ru")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    driver.quit()

