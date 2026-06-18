import socket
import requests
import re
import urllib3.util.connection as urllib3_cn
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

RESEARCH_RENTING_FORM = (
    "https://docs.google.com/forms/d/1R9nikk1z1hoxukJX_YGFFoIHiFLU_7ggySAyo1UL5fA/edit"
)
# This sandbox's IPv6 route is broken, so requests stalls trying IPv6
# addresses before falling back to IPv4. Force IPv4-only resolution.
urllib3_cn.allowed_gai_family = lambda: socket.AF_INET

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)

zilow_web_page = response.text
soup = BeautifulSoup(zilow_web_page, "html.parser")
link_property_find = soup.find_all("a", {"data-test": "property-card-link"})
link_property = [a["href"] for a in link_property_find]
print(link_property)

price_property_find = soup.find_all("span", {"data-test": "property-card-price"})
price_property = [
    re.search(r"\$[\d,]+", price.text).group() for price in price_property_find
]
print(price_property)

address_property_find = soup.find_all("address", {"data-test": "property-card-addr"})
address_property = []
for address in address_property_find:
    cleaned = re.sub(r"\s+", " ", address.text)
    cleaned = re.sub(r"\s*\|\s*", ", ", cleaned)
    address_property.append(cleaned.strip(" ,"))
print(address_property)

# Configure Selenium to stay open using the Chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# Navigate to site
driver.get(RESEARCH_RENTING_FORM)
# Alternative to using time.sleep(): use a standalone wait object
wait = WebDriverWait(driver, timeout=30)
address_field = wait.until(
    ec.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
    )
)
address_field.send_keys("fakeid")

price_field = wait.until(
    ec.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
    )
)
price_field.send_keys("3.600.000VND/month")

link_field = wait.until(
    ec.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
    )
)
link_field.send_keys("https://maps.app.goo.gl/fakedata")

send_btn = driver.find_element(By.XPATH, '//*[text()="Gửi"]')
send_btn.click()
