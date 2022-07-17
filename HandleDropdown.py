from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

def selectDropDown(country):
    driver.find_element(By.XPATH, "//select[@class='custom-select']/option[text()='"+country+"']").click()

selectDropDown("Norway")


