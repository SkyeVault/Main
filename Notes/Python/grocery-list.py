# see grocery_script.py for updated script

# before atarting, run these commands in terminal
# sudo apt update
# sudo apt install python3-pip firefox
# pip3 install selenium python-dotenv
# wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz
# tar -xvzf geckodriver-*.tar.gz
# chmod +x geckodriver
# sudo mv geckodriver /usr/local/bin/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json

# Step 1: Set up Firefox with visible window
options = webdriver.FirefoxOptions()
options.headless = False  # Show the browser window so you can solve CAPTCHA
driver = webdriver.Firefox(options=options)

# Step 2: Load the Giant Food website
driver.get("https://giantfood.com")
time.sleep(3)  # Give initial page time to load

# Step 3: Wait for manual CAPTCHA solve
def wait_for_captcha():
    print("Please solve the CAPTCHA manually in the browser window...")
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-search-button']")
            print("CAPTCHA solved. Continuing...")
            break
        except NoSuchElementException:
            time.sleep(2)

wait_for_captcha()

# Step 4: Load grocery items from local JSON file
with open("grocery_list.json") as f:
    items = json.load(f)

# Step 5: Loop through each item and search
for item in items:
    print(f"Searching: {item}")
    try:
        search_box = driver.find_element(By.CSS_SELECTOR, "input[data-testid='header-search-input']")
        search_box.clear()
        search_box.send_keys(item)
        search_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-search-button']")
        search_button.click()
        time.sleep(5)  # Wait for search results
    except Exception as e:
        print(f"Error during search: {e}")
        continue

print("Done searching all items.")
driver.quit()
