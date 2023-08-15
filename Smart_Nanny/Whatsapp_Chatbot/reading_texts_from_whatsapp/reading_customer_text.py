from function_for_reading_text import *


def reading_customer_text():
    opening_whatsapp()

    while True:
        unread_message = checking_for_unread_message()

        opening_unread_chat(unread_message)

        text = reading_chat(unread_message)

        return text
