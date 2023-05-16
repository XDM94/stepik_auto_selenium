from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link =  "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Denis")

input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Ivanov")

input3 = browser.find_element(By.NAME, "email")
input3.send_keys("Ivanov@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element(By.ID, "file")
element.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(5)
browser.quit()

