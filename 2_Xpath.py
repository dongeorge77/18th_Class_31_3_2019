from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com")
driver.find_element_by_xpath("//input[@id='u_0_j']/parent::div/child::div").send_keys("sdhgshf")