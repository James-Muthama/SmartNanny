from Smart_Nanny.Whatsapp_Chatbot.reading_texts_from_whatsapp.connecting_to_chrome_driver import driver
import time


def opening_whatsapp():
    # opening whatsapp
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    time.sleep(120)


def checking_for_unread_message():
    try:
        time.sleep(15)
        unread_message_div = driver.find_element_by_class_name("_2H6nH")

        unread_message_element = unread_message_div.find_element_by_css_selector("span")

        unread_message = unread_message_element.text

        if unread_message:
            print(unread_message)

            return int(unread_message)
        else:
            return 0
    except:
        time.sleep(60)

        checking_for_unread_message()


def opening_unread_chat(unread_message):
    chat_divs = driver.find_elements_by_class_name("_8nE1Y")

    for chat_div in chat_divs:
        # going through the structure of the whatsapp chat selection area
        div_element = chat_div.find_element_by_class_name("_2KKXC")

        sub_div_element = div_element.find_element_by_class_name("Dvjym")

        span_element = sub_div_element.find_element_by_css_selector("span")

        unread_message_div = span_element.find_element_by_class_name("_2H6nH")

        unread_message_element = unread_message_div.find_element_by_css_selector("span")

        # converting the web element for the number of unread_messages to a text then int
        unread_messages = unread_message_element.text

        # comparing it to the previous unread messages found
        if int(unread_messages) == unread_message:
            # opening the chat where the unread messages are equal to the previous unread message
            chat_div.click()

            # sleep to allow the chat to open
            time.sleep(10)

            break


def reading_chat(unread_message):
    # equates the div of the chats from the customer end to messages_from_customer
    messages_from_customer = driver.find_elements_by_class_name("_21Ahp")

    # takes the array of customer texts and gets the ones that are found at the bottom/ the unread chats
    unread_texts = messages_from_customer[-unread_message:]

    # reads each span element in the divs that contain the text from the customer
    for unread_text in unread_texts:
        span_element = unread_text.find_element_by_class_name("_11JPr")

        customer_text = span_element.find_element_by_css_selector("span")

        customer_text = customer_text.text

        return customer_text


opening_whatsapp()


unread_message = checking_for_unread_message()

opening_unread_chat(unread_message)

text = reading_chat(unread_message)