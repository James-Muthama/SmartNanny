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
        print(unread_message)
        return int(unread_message)

    except:
        time.sleep(60)

        checking_for_unread_message()


def opening_unread_chat(unread_message):
    chat_divs = driver.find_elements_by_class_name("_8nE1Y")

    for chat_div in chat_divs:
        unread_message_div = chat_div.find_element_by_class_name("_2H6nH")

        unread_message_element = unread_message_div.find_element_by_css_selector("span")

        unread_messages = unread_message_element.text

        if int(unread_messages) == unread_message:
            chat_div.click()
            time.sleep(30)
            break


def reading_chat(unread_message):
    messages_from_customer = driver.find_elements_by_class_name("_21Ahp")

    unread_texts = messages_from_customer[-unread_message:]

    for unread_text in unread_texts:
        customer_text = unread_text.find_element_by_css_selector("span._11JPr span")

        customer_text = customer_text.text

        print(customer_text)


opening_whatsapp()

time.sleep(60)

unread_message = checking_for_unread_message()

opening_unread_chat(unread_message)
