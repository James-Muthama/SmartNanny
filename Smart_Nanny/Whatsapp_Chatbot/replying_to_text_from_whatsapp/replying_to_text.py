from Smart_Nanny.Whatsapp_Chatbot.connecting_to_chrome_driver import driver
from selenium.webdriver.common.keys import Keys
from Smart_Nanny.Whatsapp_Chatbot.opening_whatsapp import opening_whatsapp
import time

opening_whatsapp()


def replying_to_text():
    # Locate the <p> element
    p_element = driver.find_element_by_css_selector(".to2l77zo .p copyable-text")

    # Clear the existing content of the <p> element
    p_element.clear()

    # Input the desired text "Hey" into the <p> element
    text_input = "Hey"
    p_element.send_keys(text_input)

    # Simulate pressing Enter to confirm the text input
    p_element.send_keys(Keys.ENTER)

    time.sleep(5)

    driver.back()