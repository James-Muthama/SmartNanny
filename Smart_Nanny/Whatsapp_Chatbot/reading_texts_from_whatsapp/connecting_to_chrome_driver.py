from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir = C:/Users/James Muthama/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)


