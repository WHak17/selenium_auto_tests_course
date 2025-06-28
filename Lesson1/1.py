import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Исходная ссылка
link = "http://suninjuly.github.io/find_link_text"

# Открываем браузер один раз
browser = webdriver.Chrome()
browser.get(link)

# Высчитываем ссылку динамически
value = str(math.ceil(math.pow(math.pi, math.e) * 10000))  # Получится примерно "224592"

# Ищем ссылку по текстовому содержимому
link_element = browser.find_element(By.LINK_TEXT, value)
link_element.click()

try:
    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Нажимаем кнопку отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Подождём немного, чтобы увидеть результат
    time.sleep(30)

finally:
    # Закроем браузер после завершения
    browser.quit()

# не забываем оставить пустую строку в конце файла