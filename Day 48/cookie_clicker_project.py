import setuptools  # Required for Python 3.12+ to provide distutils
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import time

# Initialize the driver
driver = uc.Chrome(version_main=143)
wait = WebDriverWait(driver, 20)

print("Opening Cookie Clicker...")
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    print("Waiting for language selection...")
    select_language = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
    select_language.click()
    print("Language 'EN' selected.")
except TimeoutException:
    print("Language selection timed out. It might have been skipped.")

print("Starting to click the cookie!")
cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie.click()  # Actually click the cookie!

    if time() > timeout:
        try:
            # Get affordable products using the class names we discussed
            affordable_products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            
            if affordable_products:
                # Buy the most expensive available item
                best_item = affordable_products[-1]
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")
        except Exception as e:
            print(f"Couldn't purchase items: {e}")
        
        timeout = time() + wait_time
    
    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break