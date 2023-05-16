from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary" )
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

y_element = browser.find_element (By.ID, "answer")
y_element.send_keys(y)

button2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button2.click()

time.sleep(10)
browser.quit()