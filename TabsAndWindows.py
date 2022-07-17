from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
#driver.switch_to.new_window('tab')
#driver.switch_to.new_window('window')
driver.get("https://www.opencart.com/")
driver.implicitly_wait(100)
driver.maximize_window()

print(driver.title)

#driver.find_element(By.XPATH,"//a[text()='Register']").send_keys(Keys.CONTROL+Keys.RETURN)