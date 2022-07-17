from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

driver.get("https://opensource-demo.orangehrmlive.com/")

# win1 = driver.current_window_handle
# print(win1)

driver.find_element(By.XPATH,"//a[text()=' Privacy Policy']").click()
windowsIds=driver.window_handles

# parentWin = windowsIds[0]
# childWin=windowsIds[1]
# print(parentWin)
# print(childWin)
#
# driver.switch_to.window(childWin)
# print(driver.title)
#
# driver.close()
#
# driver.switch_to.window(parentWin)
#
# print(driver.title)

# for winids in windowsIds:
#     driver.switch_to.window(winids)
#     print(driver.title)

for winids in windowsIds:
    driver.switch_to.window(winids)
    if driver.title=="OrangeHRM HR Software | Free &amp  Open Source HR Software | HRMS | HRIS":
        driver.close()




#driver.quit()