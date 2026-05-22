from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_number_article = driver.find_elements(By.XPATH,value="/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/a[1]")

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the search icon
search_icon = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
# click on the icon
search_icon.click()

#find search bar
search = driver.find_element(By.NAME, value="search")

search.send_keys("Python",Keys.ENTER)
