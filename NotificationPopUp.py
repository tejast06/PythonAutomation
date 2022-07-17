from selenium import webdriver
from selenium.webdriver.common.by import By



opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")


driver=webdriver.Chrome(options=opt)
driver.implicitly_wait(50)

driver.get("https://whatmylocation.com/")