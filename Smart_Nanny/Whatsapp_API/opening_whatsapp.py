from connecting_to_chrome_driver import driver
from checking_for_unread_message import finding_unread_message
from opening_unread_message import opening_unread_chat
import time

driver.get("https://web.whatsapp.com")

time.sleep(10)

unread_message = finding_unread_message(driver)

opening_unread_chat(unread_message, driver)


