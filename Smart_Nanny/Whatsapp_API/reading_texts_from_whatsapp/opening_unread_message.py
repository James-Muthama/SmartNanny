from Smart_Nanny.Whatsapp_API.reading_texts_from_whatsapp.finding_unread_chat import finding_unread_chat


def opening_unread_chat(unread_message, driver):
    unread_chat = finding_unread_chat(unread_message, driver)

    unread_chat.click()

