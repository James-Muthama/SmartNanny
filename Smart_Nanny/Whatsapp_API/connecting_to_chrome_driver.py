from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")
print(driver.title)


def read_message():
    unread_text = driver.find_element("")


time.sleep(10)
