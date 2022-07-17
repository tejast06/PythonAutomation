from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

driver.find_element(By.XPATH,"//input[@name='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@name='Submit']").click()

admin=driver.find_element(By.XPATH,"//li[@class='main-menu-first-level-list-item'][1]")
userMgmt=driver.find_element(By.XPATH,"//a[text()='User Management']")
users=driver.find_element(By.XPATH,"//a[text()='Users']")


act=ActionChains(driver)


act.move_to_element(admin).move_to_element(userMgmt).move_to_element(users).click().perform()
