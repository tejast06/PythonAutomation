from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

