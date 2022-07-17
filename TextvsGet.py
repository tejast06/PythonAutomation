from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")

element = driver.find_element(By.CSS_SELECTOR,"#firstName")
element.send_keys("tejas")
print(element.text)
print(element.get_attribute('value'))
