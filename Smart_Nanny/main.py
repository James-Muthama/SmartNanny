from Smart_Nanny.SmartNanny_chatbot.chat import chat
from Smart_Nanny.Whatsapp_Chatbot.reading_texts_from_whatsapp.function_for_reading_text import reading_customer_text

text = reading_customer_text()

response = chat(text)

print(response)

