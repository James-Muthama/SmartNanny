from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")
print(driver.title)


def read_message():
    unread_text = driver.find_element("l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl "
                                      "sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt "
                                      "j90th5db aumms1qt")


time.sleep(10)
