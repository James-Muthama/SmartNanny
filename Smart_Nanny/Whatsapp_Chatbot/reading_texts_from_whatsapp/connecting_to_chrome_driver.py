from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--user-data-dir=C:/Users/mywhatsapp")
driver = webdriver.Chrome(options=options)


