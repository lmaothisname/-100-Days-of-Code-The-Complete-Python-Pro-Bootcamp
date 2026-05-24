from selenium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
TINDER_URL = "https://tinder.com/"

load_dotenv()
# Configure Selenium to stay open using the Chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Removes the "Chrome is being controlled by automated software" banner — removes a flag Google checks to detect bots.
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Disables the automation extension Chrome loads when Selenium starts — another signal Google uses to detect bots
chrome_options.add_experimental_option('useAutomationExtension', False)
# Hides navigator.webdriver = true from the browser —  websites check in JavaScript to detect Selenium.
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Give Selenium it's own user profile.
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
#  use the directory you specified to store a "profile".
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
# Navigate to site
driver.get(TINDER_URL)
# Tinder's splash screen doesn't initialize properly on first load; refresh bypasses it
driver.refresh()

# Alternative to using time.sleep(): use a standalone wait object
wait =  WebDriverWait(driver, timeout=30)

# login account — skipped if already logged in via saved chrome_profile session
try:
    login_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[text()="Log in"]')))
    login_btn.click()

    login_with_google = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="c-1268805617"]/div')))
    login_with_google.click()

    #Switch to Google login window
    base_window = driver.window_handles[0]
    google_login_window = driver.window_handles[1]
    driver.switch_to.window(google_login_window)

    #Login and hit enter
    email_field = wait.until(ec.presence_of_element_located((By.NAME, "identifier")))
    email_field.clear()
    email_field.send_keys(os.environ.get("GOOGLE_EMAIL"))

    next_btn_gg_section = driver.find_element(By.XPATH, '//*[text()="Next"]')
    next_btn_gg_section.click()

    password_field = wait.until(ec.presence_of_element_located((By.NAME, "Passwd")))
    password_field.send_keys(os.environ.get("GOOGLE_PASSWORD"))

    next_btn_passwd_section = driver.find_element(By.XPATH, '//*[text()="Next"]')
    next_btn_passwd_section.click()

    #Switch back to Tinder window
    driver.switch_to.window(base_window)
except:
    # Already logged in — chrome_profile session loaded the homepage directly
    pass

for n in range(100):
  try:
    print("called")
    like_button = wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button/span/span[1]')))
    like_button.click()
  except ElementClickInterceptedException:
    try:
      match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
      match_popup.click()
    except NoSuchElementException:
      sleep(2)
driver.quit(2)