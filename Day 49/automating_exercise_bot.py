from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv
import os
import time

load_dotenv()
GYM_URL = "https://appbrewery.github.io/gym/"

# Configure Selenium to stay open using the Chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Give Selenium it's own user profile.
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
#  use the directory you specified to store a "profile".
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
# Navigate to site
driver.get(GYM_URL)

# retry wrapper
def retry(func, retries=7,description=None):
  for i in range(retries):
    print(f"Trying {description}. Attempt: {i + 1}")
    try:
      return func()
    except TimeoutException:
      if i == retries - 1:
        raise
      time.sleep(1)
      
# Alternative to using time.sleep(): use a standalone wait object
wait =  WebDriverWait(driver, timeout=2)
def login():
  # click login
  login_button = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
  login_button.click()

  # enter email
  email_input = wait.until(ec.presence_of_element_located((By.ID,"email-input")))
  email_input.clear()
  email_input.send_keys(os.environ.get("ACCOUNT_EMAIL"))

  # enter password
  password_input = driver.find_element(By.ID,value="password-input")
  password_input.clear()
  password_input.send_keys(os.environ.get("ACCOUNT_PASSWORD"))

  # submit
  submit_button = driver.find_element(By.ID,"submit-button")
  submit_button.click()

  # Wait for schedule page to load
  wait.until(ec.presence_of_element_located((By.ID,"schedule-page")))

def book_class(booking_button):
  booking_button.click()
  # Wait for button state to change - will time out if booking failed
  wait.until(lambda d: booking_button.text == "Booked")
  
# Put the entire login flow into the retry-wrapper
retry(login,description="login")
# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR,"div[id^='class-card']")

# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0
# detailed list of what happened
processed_classes = []

for card in class_cards:
  # Get the day title from the parent day group
  day_group = card.find_element(By.XPATH,"./ancestor::div[contains(@id, 'day-group-')]")
  day_title = day_group.find_element(By.TAG_NAME,"h2").text
  # Check if this is a Tuesday
  if "Tue" in day_title or "Thu" in day_title:
    # Check if this is a 6pm class
    time_text = card.find_element(By.CSS_SELECTOR,"p[id^='class-time-']").text
    if "6:00 PM" in time_text:
      # Get the class name
      class_name = card.find_element(By.CSS_SELECTOR,"h3[id^='class-name-']").text
      # Find and click the book button
      button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
      
      # Track the class details
      class_info = f"{class_name} on {day_title}"
      # Increment the counter(s)
      if button.text == "Booked":
        print(f"✓ Already booked: {class_name} on {day_title}")
        already_booked_count += 1
        processed_classes.append(f"[Booked] {class_info}")
      elif button.text == "Waitlisted":
        print(f"✓ Already on waitlist: {class_name} on {day_title}")
        already_booked_count += 1
        processed_classes.append(f"[Waitlisted] {class_info}")
      elif button.text == "Book Class":
        # Use retry for entire booking action
        retry(lambda: book_class(button), description="Booking")
        print(f"✓ Successfully booked: {class_name} on {day_title}")
        booked_count+= 1
        processed_classes.append(f"[New Booking] {class_info}")
        # Wait a moment for the button state to update
        time.sleep(0.5)
      elif button.text == "Join Waitlist":
        # Use retry for entire waitlist action
        retry(lambda: book_class(button), description="waitlisting")
        print(f"✓ Joined waitlist for: {class_name} on {day_title}")
        waitlist_count += 1
        processed_classes.append(f"[New Waitlist] {class_info}")
        # Wait a moment for the button state to update
        time.sleep(0.5)
        
# Print summary
# print("--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_count}")
# print(f"Waitlists joined: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")

# Print detailed class list
# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")
total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")


def get_my_bookings():
  # Navigate to My Bookings page
  my_booking_button = driver.find_element(By.ID,"my-bookings-link")
  my_booking_button.click()

  # Wait for My Bookings page to load
  wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

  cards = driver.find_elements(By.CSS_SELECTOR,"div[id*='card-']")
  
  if not cards:
    raise TimeoutException("No booking cards found - page may not have loaded")
  return cards
# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

# Find ALL booking cards (both confirmed and waitlist)
all_cards = retry(get_my_bookings,description="Get my bookings")

for card in all_cards:
  try:
    when_paragraph = card.find_element(By.XPATH,".//p[strong[text()='When:']]")
    when_text = when_paragraph.text
    
    # Check if it's a Tuesday or Thursday 6pm class
    if("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
      class_name = card.find_element(By.TAG_NAME,"h3").text
      print(f"  ✓ Verified: {class_name}")
      verified_count += 1
  except NoSuchElementException:
    pass
  
# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")


  