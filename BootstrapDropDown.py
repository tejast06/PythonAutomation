from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(60)

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countriesList=driver.find_elements(By.XPATH,"//ul[@class='select2-results__options']/li")
print(len(countriesList))

for i in countriesList:
    if i.text == "Indonesia":
        i.click()
        break



