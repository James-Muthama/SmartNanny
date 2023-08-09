from selenium.webdriver.common.by import By


def checking_for_unread_message(driver):
    unread_message_element = driver.find_element(By.CLASS_NAME,
                                                 "l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp "
                                                 "dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg "
                                                 "ap18qm3b ikwl5qvt j90th5db aumms1qt")

    unread_message = unread_message_element.txt

    print(unread_message)
