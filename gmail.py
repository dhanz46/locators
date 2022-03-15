from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//dhana//PycharmProjects//pythonProject//driver//chromedriver.exe")
#Implicit waits

driver.implicitly_wait(10)

driver.get("http://google.com")

driver.find_element_by_name("q").send_keys("automation")
driver.find_element_by_name("btnk1").click()

print("test completed")
driver.close()
driver.quit()