from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

y_element = browser.find_element (By.ID, "answer")
y_element.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option2 = browser.find_element(By.ID, "robotsRule")
option2.click()

option3 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
option3.click()

time.sleep(5)
browser.quit()