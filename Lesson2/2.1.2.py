import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_valuex = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_element = x_valuex.get_attribute("valuex")
    y = calc(x_element)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла