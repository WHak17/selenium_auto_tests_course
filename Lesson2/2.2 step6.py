import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элементов по id
    input_v = browser.find_element(By.ID, "input_value")
    input_v_text = input_v.text
    y = calc(input_v_text)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    # Нажатие кнопки отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Пауза для копирования результатов
    time.sleep(30)
    # Закрытие браузера
    browser.quit()

# не забываем оставить пустую строку в конце файла