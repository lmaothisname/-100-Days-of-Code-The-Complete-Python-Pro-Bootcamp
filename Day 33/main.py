import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 10.8745695 # Your latitude
MY_LONG = 106.80874498518394 # Your longitude
MY_EMAIL = "trancaoanhkiet@gmail.com"
PASSWORD = "lrkb zoks vdpq laxp"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
min_lat = MY_LAT - 5
max_lat = MY_LAT + 5
min_long = MY_LONG - 5
max_long = MY_LONG + 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if min_lat <= iss_latitude <= max_lat and min_long <= iss_longitude <= max_long and (time_now >= sunset or time_now <= sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs="lmaothiscoach@gmail.com",msg= "Subject:Look Up☝️\n\nThe ISS is above you in the sky")
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



