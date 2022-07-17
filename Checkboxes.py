from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

# monday = driver.find_element(By.CSS_SELECTOR,"#monday")
# monday.click()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for i in checkboxes:
#     week=i.get_attribute('id')
#     if week=='monday'or week=='sunday':
#         i.click()

#last 2 checkboxes:
# for i in range(len(checkboxes)-2,len(checkboxes)):  #range(5,7)
#     checkboxes[i].click()
#
# #first 2 checkboxes:
# for i in range(len(checkboxes)):
#     if i<2:
#       checkboxes[i].click()


#clear all checkboxes
for i in checkboxes:
    i.click()

for i in checkboxes:
    if i.is_selected():
        i.click()
