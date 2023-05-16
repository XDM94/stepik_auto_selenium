from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver.find_element(By.XPATH, '//*[@type="submit"]/div[6]/input').click()
input1 = browser.find_element(By.XPATH, '//div[@type()="submit"]/input')
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.XPATH, '//div[@id()="submit_button"]')
button.click()

browser.quit()