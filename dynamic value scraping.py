import re
import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SAMPLE_INTERVAL_SECONDS = 2
VALUE_LOCATOR = (By.XPATH, "/html/body/div[1]/p[3]")


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
        output_file = Path(__file__).with_name("dynamic_values.txt")
        next_sample = time.monotonic()

        while True:
            text_element = wait.until(
                EC.presence_of_element_located(VALUE_LOCATOR)
            )
            value = clean_text(text_element.text)
            timestamp = datetime.now().isoformat(timespec="seconds")
            output_line = f"{timestamp}: {value}"

            print(output_line, flush=True)
            with output_file.open("a", encoding="utf-8") as file:
                file.write(output_line + "\n")

            next_sample += SAMPLE_INTERVAL_SECONDS
            driver.refresh()
            wait.until(EC.presence_of_element_located(VALUE_LOCATOR))
            time.sleep(max(0, next_sample - time.monotonic()))
    except KeyboardInterrupt:
        print("\nScraping stopped.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
