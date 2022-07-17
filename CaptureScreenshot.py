from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(100)
driver.maximize_window()

driver.save_screenshot("C:\\Users\\Hp\\PycharmProjects\\PythonAutomation\\testcases\\homepage.png")