from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

alertWindow=driver.switch_to.alert
print(alertWindow.text)
alertWindow.send_keys("welcome")

alertWindow.dismiss()
