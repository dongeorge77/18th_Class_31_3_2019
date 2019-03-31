from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com")

driver.find_element_by_partial_link_text("Forgotten account?").click()