import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")

# actualTitle = driver.title
# expectedTitle = "Google"
#
# print(driver.title)
#
#
# if actualTitle==expectedTitle:
#     print("page title is correct")
#
#
# logo=driver.find_element(By.CSS_SELECTOR,"[alt='Google']")
# print(logo.is_displayed())

time.sleep(5)



checkbox = driver.find_element(By.CSS_SELECTOR,"#gender-radio-1")
checkbox.click()
print(checkbox.is_selected())