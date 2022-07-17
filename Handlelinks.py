from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)


driver.get("https://demo.nopcommerce.com/")

#driver.find_element(By.LINK_TEXT,"Digital downloads").click()

links = driver.find_elements(By.TAG_NAME,'a')
print(len(links))

for i in links:
    print(i.text)