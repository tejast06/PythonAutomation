from logging import log

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome("F:\Chromedriver\chromedriver.exe")
driver=webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")


driver.find_element(By.CSS_SELECTOR, '.email.valid').clear()
driver.find_element(By.CSS_SELECTOR, '.email.valid').send_keys("admin@yourstore.com")


driver.find_element(By.CSS_SELECTOR, '#Password').clear()
driver.find_element(By.CSS_SELECTOR, '#Password').send_keys("admin")


driver.find_element(By.CSS_SELECTOR,'.button-1.login-button').click()


actualTitle=driver.title
expectedTitle="Dashboard / nopCommerce administration"

if actualTitle==expectedTitle:
    print("Validation passed successfully")
else:
    print("Validation failed")



driver.close()