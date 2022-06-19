from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver/geckodriver.exe")
driver.get("https://192.168.15.91/auth.html")
driver.implicitly_wait(10)
driver.find_element_by_id("userName").send_keys("190570107077")
driver.find_element_by_name("pwd").send_keys("Arp@13042002")
driver.find_element_by_name("Submit").click()

