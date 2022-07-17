

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get("https://www.google.com/?gws_rd=ssl")

myWait = WebDriverWait(driver,10)


searchField = driver.find_element(By.XPATH,"//input[@name='q']")
searchField.send_keys("Selenium")
searchField.submit()

link = myWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
link.click()

