import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MainPage():
    def check_reg_data(link):
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
        return welcome_text

class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(MainPage.check_reg_data("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "Регистрация неверная!!!")

    def test_reg2(self):
        self.assertEqual(MainPage.check_reg_data("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "Регистрация неверная!!!")

    def test_reg3(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(MainPage.check_reg_data(link), "Congratulations! You have successfully registered!", "Регистрация неверная!!!")


if __name__ == "__main__":
    unittest.main()
