from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://www.countries-ofthe-world.com/all-countries.html")

#scroll down by pixel:
# driver.execute_script("window.scrollBy(0,1500)","")
# value=driver.execute_script("return window.pageYOffset;")
# print(value)

#scroll down till elemnet is visible
ele=driver.find_element(By.XPATH,"//li[text()='Switzerland']")
driver.execute_script("arguments[0].scrollIntoView();",ele)




