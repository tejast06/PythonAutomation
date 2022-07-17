from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.google.com/?gws_rd=ssl")
driver.implicitly_wait(10)


searchField = driver.find_element(By.XPATH,"//input[@name='q']")
searchField.send_keys("Selenium")
searchField.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
