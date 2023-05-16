from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

y_element = browser.find_element (By.ID, "answer")
y_element.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()

option3 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
option3.click()

time.sleep(5)

browser.quit()

















