from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("F:\Chromedriver\chromedriver.exe")
driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")

links = driver.find_elements(By.TAG_NAME,'a')
print(len(links))