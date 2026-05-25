from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv
import time
load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
SPEED_TEST_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/"


class InternetSpeedTwitterBot:
  def __init__(self):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_experimental_option("detach", True)
    # Removes the "Chrome is being controlled by automated software" banner — removes a flag Google checks to detect bots.
    self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Disables the automation extension Chrome loads when Selenium starts — another signal Google uses to detect bots
    self.chrome_options.add_experimental_option('useAutomationExtension', False)
    # Hides navigator.webdriver = true from the browser —  websites check in JavaScript to detect Selenium.
    self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Give Selenium it's own user profile.
    self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    #  use the directory you specified to store a "profile".
    self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
    self.driver = webdriver.Chrome(options=self.chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=90)
    self.down = 0
    self.up = 0
  
  def get_internet_speed(self):
    self.driver.get(SPEED_TEST_URL)
    # Give the page 3 seconds to open any ad popups before we check for extra tabs
    time.sleep(3)
    # Save the speedtest tab so we can return to it after closing popups
    main = self.driver.window_handles[0]
    # Close every extra tab (ads/popups) — window_handles[1:] skips the first (main) tab
    for handle in self.driver.window_handles[1:]:
      self.driver.switch_to.window(handle)
      self.driver.close()
    # Refocus the driver on the speedtest tab
    self.driver.switch_to.window(main)
    # Wait for the Go button to be clickable, then start the test
    self.go_btn = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a .start-text")))
    self.go_btn.click()
    # Poll until the download value is real (not empty, zero, or placeholder)
    self.down = self.wait.until(
      lambda d: d.find_element(By.CSS_SELECTOR, "div .download-speed").text
      if d.find_element(By.CSS_SELECTOR, "div .download-speed").text not in ("", "0.00", "0", "—")
      else False
    )
    # Same for upload
    self.up = self.wait.until(
      lambda d: d.find_element(By.CSS_SELECTOR, "div .upload-speed").text
      if d.find_element(By.CSS_SELECTOR, "div .upload-speed").text not in ("", "0.00", "0", "—")
      else False
    )
    print(self.down)
    print(self.up)

  def tweet_at_provider(self):
    self.driver.get(X_URL)
    try:
      # Short 5s timeout — if the login iframe isn't found quickly, we're already logged in
      login_wait = WebDriverWait(self.driver, timeout=5)
      # The "Continue with Google" button lives inside a Google-served iframe, so we must switch into it first
      iframe = login_wait.until(ec.presence_of_element_located((By.CLASS_NAME, "L5Fo6c-PQbLGe")))
      self.driver.switch_to.frame(iframe)
      btn = login_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="button"]')))
      btn.click()
      # Step back out of the iframe to the main page
      self.driver.switch_to.default_content()
      # Google OAuth opens in a new window — save both handles so we can switch between them
      self.base_window = self.driver.window_handles[0]
      self.google_login_window = self.driver.window_handles[1]
      self.driver.switch_to.window(self.google_login_window)

      # Enter email and wait a moment before clicking Next so the button is ready
      self.email_field = self.wait.until(ec.presence_of_element_located((By.NAME,"identifier")))
      self.email_field.send_keys(os.environ.get("X_EMAIL"))
      time.sleep(2)
      continue_btn = self.driver.find_element(By.XPATH, '//*[text()="Next"]')
      continue_btn.click()

      # Enter password and wait before clicking Next
      self.passwd_field = self.wait.until(ec.presence_of_element_located((By.NAME,"Passwd")))
      self.passwd_field.send_keys(os.environ.get("X_PASSWORD"))
      time.sleep(2)
      continue_btn = self.driver.find_element(By.XPATH, '//*[text()="Next"]')
      continue_btn.click()

      # Switch back to the X tab after login completes
      self.driver.switch_to.window(self.base_window)
    except:
      # Login iframe not found — session already exists in chrome_profile, skip login
      pass

    # Click the compose button in the left sidebar to open the x dialog
    self.create_post_btn = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="SideNav_NewTweet_Button"]')))
    self.create_post_btn.click()

    self.context = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    # Wait for the x textarea to appear inside the compose dialog
    self.x_box = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
    # click() focuses the contenteditable div, send_keys() types the message — chained so both fire together
    ActionChains(self.driver).click(self.x_box).send_keys(self.context).perform()

    # Click Post to publish the x
    self.post_btn = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))
    self.post_btn.click()
    
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()