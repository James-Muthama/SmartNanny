from opening_whatsapp import opening_whatsapp
from Smart_Nanny.Whatsapp_Chatbot.reading_texts_from_whatsapp.connecting_to_chrome_driver import driver
import pickle
import time

opening_whatsapp()

time.sleep(120)

cookies = driver.get_cookies()

pickle.dump(cookies, open("cookies.pkl", "wb"))



