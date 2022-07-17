from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(50)

#driver.get("https://jqueryui.com/datepicker/")

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.switch_to.frame(0)

def selectCalendar(month,year,date):
    driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']/option[text()='"+month+"']").click()
    driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']/option[text()='"+year+"']").click()
    driver.find_element(By.XPATH,"//a[text()='"+date+"']").click()

driver.find_element(By.XPATH,"//input[@id='dob']").click()
selectCalendar("Dec","1990","6")








#mm/dd/yyyy
#driver.find_element(By.CSS_SELECTOR,".hasDatepicker").send_keys("12/06/1990")



# driver.find_element(By.CSS_SELECTOR,".hasDatepicker").click()
# month="August"
# date="15"
# yr="2022"



# while True:
#     mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#
#     if mon==month and year==yr:
#         break
#     else:
#         driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']").click()
#
# #select date:
#
#     dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
#     for ele in dates:
#         if ele.text==date:
#             ele.click()
#             break





