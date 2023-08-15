from Smart_Nanny.Whatsapp_Chatbot.connecting_to_chrome_driver import driver
import time


def opening_whatsapp():
    # opening whatsapp
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    time.sleep(120)
