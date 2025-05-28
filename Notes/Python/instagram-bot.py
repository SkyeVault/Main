# Disclaimer

#This project is intended for **educational and testing purposes only**.

# Automating interactions with Instagram via unofficial methods may violate Instagram’s Terms of Service. The author assumes no responsibility for how this script is used. Use at your own risk, and only with test accounts or platforms you own.

# Do not use this tool to spam, harass, or violate platform guidelines.


import random
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException

username = input("Enter your Instagram username: ")
password = getpass("Enter your Instagram password: ")

# 💬 Comment list
comments = [
    "This is great 👏", "🔥🔥🔥", "Love your feed!", "Wow 😍", 
    "Awesome vibe 🌿", "So good!", "Beautiful post", "Incredible 🧡"
]

# 🔁 Hashtag list to rotate through
hashtags = [
    "nature", "travel", "art", "music", "photography", 
    "design", "architecture", "coding", "handmade", "landscape"
]

profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/114.0")
profile.set_preference("network.http.use-cache", False)

options = Options()
# options.headless = True

browser = webdriver.Firefox(firefox_profile=profile, options=options)
browser.implicitly_wait(10)

def login():
    browser.get("https://www.instagram.com/accounts/login/")
    time.sleep(random.uniform(3, 6))
    user_input = browser.find_element(By.NAME, 'username')
    pass_input = browser.find_element(By.NAME, 'password')
    user_input.send_keys(username)
    pass_input.send_keys(password)
    login_btn = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    time.sleep(random.uniform(4, 8))

def interact_with_hashtag(tag):
    print(f"\n🔁 Switching to hashtag: #{tag}")
    browser.get(f"https://www.instagram.com/explore/tags/{tag}/")
    time.sleep(random.uniform(4, 7))
    
    posts = browser.find_elements(By.CSS_SELECTOR, "article a")
    if not posts:
        print("⚠️ No posts found.")
        return

    for i in range(min(random.randint(5, 10), len(posts))):
        try:
            posts[i].click()
            time.sleep(random.uniform(3, 6))

            like_button = browser.find_element(By.XPATH, "//span[contains(@class, 'like')]/..")
            like_button.click()
            print("❤️ Liked")

            comment_field = browser.find_element(By.CSS_SELECTOR, "form textarea")
            comment_field.click()
            time.sleep(1)
            comment_field.send_keys(random.choice(comments))
            post_btn = browser.find_element(By.XPATH, "//form//button[@type='submit']")
            post_btn.click()
            print("💬 Commented")

            if random.random() > 0.6:
                follow_btn = browser.find_element(By.XPATH, "//button[text()='Follow']")
                follow_btn.click()
                print("➕ Followed")

            time.sleep(random.uniform(4, 8))
            close_btn = browser.find_element(By.XPATH, "//div[@aria-label='Close']")
            close_btn.click()

            wait = random.uniform(10, 30)
            print(f"⏳ Waiting {wait:.1f} sec before next post...")
            time.sleep(wait)

        except NoSuchElementException:
            print("⚠️ Error or missing element, skipping...")
            browser.get(f"https://www.instagram.com/explore/tags/{tag}/")
            time.sleep(random.uniform(3, 5))

def run_loop():
    login()
    while True:
        random.shuffle(hashtags)
        for tag in hashtags:
            interact_with_hashtag(tag)
            delay = random.uniform(120, 300)  # 2–5 min pause between tags
            print(f"🛌 Resting for {delay:.1f} sec before switching hashtags...\n")
            time.sleep(delay)

def shutdown():
    print("Shutting down browser...")
    browser.quit()

if __name__ == "__main__":
    try:
        run_loop()
    except KeyboardInterrupt:
        print("\n🛑 Script interrupted by user.")
        shutdown()