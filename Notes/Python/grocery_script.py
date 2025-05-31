
import json
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# Proxy list (free proxies - replace with working IP:PORT combinations)
proxies = [
    "51.158.123.35:8811",
    "51.158.68.68:8811",
    "195.154.255.194:80"
]

def get_random_proxy():
    return random.choice(proxies)

def create_driver(proxy=None):
    options = uc.ChromeOptions()
    if proxy:
        options.add_argument(f'--proxy-server=http://{proxy}')
    driver = uc.Chrome(options=options)
    return driver

def load_grocery_list(path="grocery_list.json"):
    with open(path, "r") as f:
        return json.load(f)

def search_item(driver, item):
    try:
        print(f"Searching: {item}")
        driver.get("https://giantfoodstores.com")
        time.sleep(random.uniform(5, 8))  # Wait for page load
        search_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-search-button']")
        search_button.click()
        search_input = driver.find_element(By.NAME, "searchTerm")
        search_input.send_keys(item)
        search_input.submit()
        time.sleep(random.uniform(3, 6))
        print(f"Finished searching: {item}")
    except NoSuchElementException as e:
        print(f"Error during search: {e}")
        return False
    except WebDriverException as e:
        print(f"WebDriver error: {e}")
        return False
    return True

def main():
    grocery_items = load_grocery_list()
    max_retries = 3

    for attempt in range(max_retries):
        proxy = get_random_proxy()
        print(f"Attempt {attempt + 1} using proxy: {proxy}")
        try:
            driver = create_driver(proxy)
            for item in grocery_items:
                success = search_item(driver, item)
                if not success:
                    print("Skipping failed item.")
                time.sleep(random.uniform(2, 5))
            driver.quit()
            break  # Exit loop after success
        except Exception as e:
            print(f"Error with proxy {proxy}: {e}")
            if 'driver' in locals():
                driver.quit()
            time.sleep(2)
    else:
        print("All proxies failed. Manual intervention required.")

if __name__ == "__main__":
    main()
