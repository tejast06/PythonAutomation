import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_elements(By.TAG_NAME,'a')


for links in allLinks:
    url = links.get_attribute('href')
    response = requests.head(url)
    if response.status_code >=400:
        print(url +"is broken link")