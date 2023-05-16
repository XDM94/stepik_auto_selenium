from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary" )
button.click()

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

y_element = browser.find_element (By.ID, "answer")
y_element.send_keys(y)

button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button2.click()

time.sleep(5)
browser.quit()