from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://text-compare.com/")

text1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
text2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

text1.send_keys("welcome to selenium")

act=ActionChains(driver)

#ctrl+a select the text
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB).perform()

#ctrl V paste the text
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_down(Keys.CONTROL).perform()