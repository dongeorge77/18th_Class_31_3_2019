from selenium import webdriver

PROXY = "localhost:1231"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com")

driver.find_element_by_partial_link_text("Forgotten account?").click()