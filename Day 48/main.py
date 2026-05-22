from selenium import webdriver
from selenium.webdriver.common.by import By
# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {index: {"time":event_times[index].text, "name":event_names[index].text}for index in range(len(event_times))}
print(events)
# driver.close()