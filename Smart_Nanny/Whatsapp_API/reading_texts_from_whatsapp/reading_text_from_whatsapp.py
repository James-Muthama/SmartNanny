from Smart_Nanny.Whatsapp_API.reading_texts_from_whatsapp.connecting_to_chrome_driver import driver
from Smart_Nanny.Whatsapp_API.reading_texts_from_whatsapp.checking_for_unread_message import finding_unread_message
from Smart_Nanny.Whatsapp_API.reading_texts_from_whatsapp.opening_unread_message import opening_unread_chat
from Smart_Nanny.Whatsapp_API.reading_texts_from_whatsapp.reading_latest_text import reading_latest_text
import time


def reading_text_from_whatsapp():
    driver.get("https://web.whatsapp.com")

    time.sleep(10)

    unread_message = finding_unread_message(driver)

    opening_unread_chat(unread_message, driver)

    text = reading_latest_text(driver)

    return text
