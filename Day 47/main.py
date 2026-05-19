import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib
PRICE_EXPECT = 6000000
load_dotenv()

URL = "https://www.amazon.com/DJI-Essential-Waterproof-Performance-Long-Lasting/dp/B0DS2B3P2B/ref=sr_1_1?crid=17EFT5Q340ARP&dib=eyJ2IjoiMSJ9.7C42-cYWskQw1WrUx8V7twnGAVt1Y4CQrfDkhUqxhOdFR6952bjwZoxj9lJ3chHA7CVH9uxQi1c_J-Nnt2K8JNX4YbDUKY1GdGZtU2Uqm3hbD2_fumROksaJ3lF5q-GKmid9cS_vRyF4qQ7FhFZfJleoZP2ridQtluk6A87HdWSgJwPnheOsYpLYb-n9fQY0JZN8VqfiHhJ8ZvYFSEUBrDgaoIZaXoi-URtNIXa2oA4.aqy6QtGuI2DCBVCGxQnfTF46KCStWfeNZh2xYY6yoo4&dib_tag=se&keywords=dji%2Baction&qid=1779172014&sprefix=dji%2Bactio%2Caps%2C382&sr=8-1&th=1"
header = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

cookies = {
  "csm-hit": "tb:GGTM0RF97F10CGPP5MN4+s-M907HKTN6MZJQPZV4NS8|1779173841993&t:1779173841993&adb:adblk_no",
  "i18n-prefs": "VND",
  "session-id": "141-2685582-8645109",
  "session-id-time": "2082787201l",
  "session-token": "7JGl+IuhFPDBBaag4UpqDe0JYttFnuyPvneGPb/nmt4UUK7ptR7AirWRT7GjE9r+QX//Y2v3gZKc3DnurEzhupKxtk41BpuLD/zh7XB7SlEdMHd+Bi8Zolh0UWtr4xTtuMHjXF2wG9Iam2zmiM2aUdLuCVXuJvCkwpoKrCq0mnVS84XT49HVtB/586+h57AZzVRqtKl6pGDtXQVVtnhWQcQ7MB8B7p+C",
  "ubid-main": "131-9294726-6927469"
}

response = requests.get(url=URL,cookies=cookies, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(name="span", class_="aok-offscreen").get_text()
price_withou_currency = price.split("VND")[1]
price_as_float = float(price_withou_currency.replace(",",""))

# get the product title
title = soup.find(name="span", id="productTitle").get_text().strip()

if price_as_float < PRICE_EXPECT:
  message = f"{title} is on sale for {price}!"
  with smtplib.SMTP(os.getenv("METHOD_EMAIL")) as connection:
    connection.starttls()
    connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("EMAIL_PASSWORD"))
    connection.sendmail(from_addr=os.getenv("MY_EMAIL"), to_addrs="lmaothiscoach@gmail.com", msg=f"Subject: Amazon Price Alert!\n\n {message}\n{URL}".encode("utf-8"))
