# see grocery_script.py for updated script

# before atarting, run these commands in terminal
# sudo apt update
# sudo apt install python3-pip firefox
# pip3 install selenium python-dotenv
# wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz
# tar -xvzf geckodriver-*.tar.gz
# chmod +x geckodriver
# sudo mv geckodriver /usr/local/bin/

import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Step 1: Visit Giant Food Stores
driver.get("https://giantfoodstores.com/")
time.sleep(5)  # Let the page load fully

# Step 2: Accept cookies if the popup exists
try:
    accept_btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_btn.click()
    print("Cookies accepted.")
    time.sleep(2)
except:
    print("No cookie banner found.")

# Step 3: Find the search bar and search for 'bananas'
try:
    search_icon = driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-search-button']")
    search_icon.click()
    time.sleep(2)

    search_input = driver.find_element(By.ID, "search-input")
    search_input.send_keys("bananas")
    search_input.send_keys(Keys.RETURN)
    print("Searching for bananas...")
    time.sleep(6)

    # Step 4: Confirm that results appear
    results = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='product-card']")
    if results:
        print(f"Found {len(results)} results for bananas.")
    else:
        print("No search results found.")

except Exception as e:
    print("Error during search:", e)

# Step 5: Finish
time.sleep(5)
driver.quit()