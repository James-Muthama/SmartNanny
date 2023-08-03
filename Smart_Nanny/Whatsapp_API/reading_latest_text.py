from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def reading_latest_text(driver):
    try:
        all_texts = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "_11JPr selectable-text copyable-text"))
        )
        if all_texts:
            latest_text = all_texts[-1]

            return latest_text

    except:
        print("Cannot find texts")
