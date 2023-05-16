from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x,y):
  return str(int(x)+int(y))


num_1 = browser.find_element(By.ID, "num1")
x = num_1.text

num_2 = browser.find_element(By.ID, "num2")
y = num_2.text

z = calc(x, y)


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(z)


button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()


time.sleep(5)

browser.quit()

