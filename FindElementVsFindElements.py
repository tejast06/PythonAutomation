from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")

element = driver.find_element(By.XPATH,"//div[@class='left-pannel']/div/div")
print(element.text)

elements = driver.find_elements(By.XPATH,"//div[@class='left-pannel']/div/div")
print(len(elements))
for ele in elements:
    print(ele.text)


