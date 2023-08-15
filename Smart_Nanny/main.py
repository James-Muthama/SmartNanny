from Smart_Nanny.SmartNanny_chatbot.chat import chat
from Smart_Nanny.Whatsapp_Chatbot.opening_whatsapp import opening_whatsapp
from Smart_Nanny.Whatsapp_Chatbot.reading_texts_from_whatsapp.reading_customer_text import reading_customer_text

opening_whatsapp()

while True:
    text = reading_customer_text()

    response = chat(text)

    
