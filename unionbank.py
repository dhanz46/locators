from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C://Users//dhana//PycharmProjects//pythonProject//driver//chromedriver.exe")
#Implicit waits

driver.implicitly_wait(10)

driver.get("")
driver.find_element_by_class_name("").send_keys("dhananjaybr10@gmail.com")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_name("login")

print("text completed")
time.sleep(10)
driver.close()
driver.quit()