from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://testautomationpractice.blogspot.com/")


#number of rows and columns
row=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))

col=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))
#
# print(row,col)
#
# #specific row and column data
# ele1=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")
# print(ele1.text)

#read data base on condition
for r in range(2,row+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author=="Mukesh":
        book=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        print(book,author)





