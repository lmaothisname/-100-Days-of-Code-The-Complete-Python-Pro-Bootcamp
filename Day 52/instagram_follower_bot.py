from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import time
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()
SIMILAR_ACCOUNT = "patrickpetrukaa"
INSTA_URL = "https://www.instagram.com/accounts/login/"

class InstaFollower:
  def __init__(self):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_experimental_option("detach", True)
    # Removes the "Chrome is being controlled by automated software" banner — removes a flag Google checks to detect bots.
    self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Disables the automation extension Chrome loads when Selenium starts — another signal Google uses to detect bots.
    self.chrome_options.add_experimental_option('useAutomationExtension', False)
    # Hides navigator.webdriver = true from the browser — websites check this in JavaScript to detect Selenium.
    self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Give Selenium its own user profile so login sessions are saved between runs.
    self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
    self.driver = webdriver.Chrome(options=self.chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=30)
    time.sleep(2)

  def login(self):
    self.driver.get(INSTA_URL)
    # Only log in if we're not already logged in (no saved session in chrome_profile).
    if "/login" in self.driver.current_url:
      email_box = self.wait.until(ec.element_to_be_clickable((By.NAME, "email")))
      email_box.send_keys(os.environ.get("INSTA_EMAIL"))
      pass_box = self.driver.find_element(By.NAME, "pass")
      pass_box.send_keys(os.environ.get("INSTA_PASSWORD"))
      time.sleep(2)
      login_btn = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log In"]')
      login_btn.click()

      # Extend timeout to 60s so the user has time to complete any verification challenge manually.
      self.wait = WebDriverWait(self.driver, timeout=60)
      self.wait.until(lambda d: "/login" not in d.current_url and "challenge" not in d.current_url)

      # Dismiss the "Save login info?" prompt.
      save_login_info = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[role="button"]')))
      save_login_info.click()

      # Dismiss the "Turn on notifications?" prompt.
      ask_notification = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]')))
      ask_notification.click()

  def find_followers(self):
    # Open the search panel and type the target account name.
    search_btn = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Search"]')))
    search_btn.click()
    time.sleep(2)

    search_box = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search input"]')))
    search_box.send_keys(SIMILAR_ACCOUNT)
    time.sleep(1)

    # Click the matching account from the search results using its href.
    account = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/{SIMILAR_ACCOUNT}/"]')))
    account.click()

    # Click the followers count link to open the followers modal.
    followers_link = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[.//span[contains(text(),"followers")]]')))
    followers_link.click()
    time.sleep(2)

    # The XPath of the modal scroll container may change over time — update accordingly.
    modal_xpath = "/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
    modal = self.wait.until(ec.presence_of_element_located((By.XPATH, modal_xpath)))

    # Scroll the modal to the bottom repeatedly to trigger lazy-loading of more followers.
    # arguments[0] refers to the modal element passed to execute_script.
    # Setting scrollTop = scrollHeight jumps the scroll position to the very bottom.
    for _ in range(2):
      self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
      time.sleep(2)

  def follow(self):
    # Find all visible "Follow" buttons inside the modal.
    all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button._aswp._aswr._aswu._asw_._asx2')
    for button in all_buttons:
      try:
        # Use JS click to bypass the dialog overlay that blocks normal Selenium clicks.
        self.driver.execute_script("arguments[0].click()", button)
        time.sleep(1.1)
      except ElementClickInterceptedException:
        # If a "follow back" confirmation dialog appears, dismiss it.
        cancel_btn = self.driver.find_element(By.XPATH, '//[button[contains(text(),"Cancel")]]')
        cancel_btn.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
