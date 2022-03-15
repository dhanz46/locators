from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C://Users//dhana//PycharmProjects//pythonProject//driver//chromedriver.exe")
#Implicit waits

driver.implicitly_wait(10)

driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_class_name("input.r4.wide.mb16.mt8.username").send_keys("dhananjaybr10@gmail.com")
driver.find_element_by_id("password").send_keys("12345678")
driver.find_element_by_name("login")

print("text completed")
time.sleep(10)
driver.close()
driver.quit()






