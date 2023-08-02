from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")
print(driver.title)
