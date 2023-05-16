from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("EMAIL")
    input4 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
    input4.send_keys("999")
    input5 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.second_block > div.form-group.second_class > input')
    input5.send_keys("My Address")
    time.sleep(5)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)


    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    browser.quit()