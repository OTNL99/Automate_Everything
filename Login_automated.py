from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")  # Run in background (optional)

    driver = webdriver.Chrome(options=options)  # or use any other browser driver
    driver.get("https://www.pythonanywhere.com/")  # Replace with the URL you want to scrape
    return driver

def main():
    driver = get_driver()
    # Scrape simple text from the webpage
    text_element = driver.find_element(by="id",value="id_username").send_keys("your_username")  # Replace with the actual username
    text_element = driver.find_element(by="id",value="id_password").send_keys("your_password" + Keys.RETURN)  # Replace with the actual password
    #text_element = driver.find_element(by="id",value="id_login").click()
    #print(driver.current_url)
    time.sleep(5)  # Wait for the page to load

    driver.find_element(by="xpath",value="/html/body/div[1]").click()
    print(driver.current_url)
   
print(main())
