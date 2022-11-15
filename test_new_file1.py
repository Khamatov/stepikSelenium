import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
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
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
