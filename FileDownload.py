from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


def chromeSetUp():

    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)

    return driver


driver=chromeSetUp()
driver.get("https://file-examples.com/index.php/sample-documents-download/")


driver.implicitly_wait(50)

driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/a[1]").click()


