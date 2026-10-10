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
    driver.get("https://titan22.com/account/login?srsltid=AU7gw4W3VNJZ2AOL2xy5Zd9iVWrgu6tqiE0OUatkJ_Y5-q8Ewe-g56Wf")  # Replace with the URL you want to scrape
    return driver

def main():
    driver = get_driver()
    # Scrape simple text from the webpage
    driver.find_element(by="id",value="CustomerEmail").send_keys("lacexontechnology@gmail.com")  # Replace with the actual username
    time.sleep(3)
    driver.find_element(by="id",value="CustomerPassword").send_keys("qwertyuiop" + Keys.RETURN)  # Replace with the actual password
    time.sleep(3)
    driver.find_element(
        by="xpath",
        value="/html/body/header/div[1]/div[1]/div/div[2]/nav[1]/ul/li[2]/a"
        ).click()
    time.sleep(10)
    #text_element = driver.find_element(by="id",value="id_login").click()
    print(driver.current_url)
    

    #driver.find_element(by="xpath",value="/html/body/header/div[1]/div[1]/div/div[2]/nav[1]/ul/li[2]/a").click()
    #print(driver.current_url)
   
print(main())
