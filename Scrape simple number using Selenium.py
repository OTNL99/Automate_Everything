import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    match = re.search(r"[-+]?\d*\.?\d+", text)
    if not match:
        raise ValueError(f"No numeric value found in text: {text!r}")
    return float(match.group())


def main():
    driver = get_driver()
    try:
        wait = WebDriverWait(driver, 10)
        text_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/p[3]") )
        )
        value = clean_text(text_element.text)
        print(value)
        return value
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
