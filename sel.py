from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 15)
    price_condition = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    wait.until(price_condition)
    first = browser.find_element(By.CSS_SELECTOR, "#book")
    first.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = input1.text
    print(x)
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()