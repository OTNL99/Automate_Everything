from selenium import webdriver

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
    text_element = driver.find_element(
        by="xpath",
        value="//*[@id='id_buttons']/div/div/div[1]/p[1]"
    )
    return text_element.text  # Return the scraped text

print(main())
