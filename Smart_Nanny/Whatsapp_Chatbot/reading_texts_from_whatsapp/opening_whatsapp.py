from Smart_Nanny.Whatsapp_Chatbot.reading_texts_from_whatsapp.connecting_to_chrome_driver import driver
import time


def opening_whatsapp():
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")


def checking_for_unread_message():
    try:
        unread_message_div = driver.find_element_by_class_name("_2H6nH")

        unread_message_element = unread_message_div.find_element_by_css_selector("span")

        unread_message = unread_message_element.text

        return int(unread_message)

    except:
        time.sleep(60)

        checking_for_unread_message()

def opening_unread_chat(unread_message):
    chat_div = driver.find_element_by_class_name("_2H6nH")


opening_whatsapp()

time.sleep(60)

unread_message = checking_for_unread_message()
