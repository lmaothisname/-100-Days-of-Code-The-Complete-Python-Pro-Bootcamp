import smtplib
import random
import datetime

with open(r"D:\Python\Day 32\quotes.txt") as file:
    list_quotes = [line.strip() for line in file]

select_quotes = random.choice(list_quotes)
my_email = "trancaoanhkiet@gmail.com"
password = "lrkb zoks vdpq laxp"
now = datetime.datetime.now()
day_of_week = now.weekday()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    if day_of_week == 2:
        connection.sendmail(from_addr=my_email,to_addrs="lmaothiscoach@gmail.com",msg=f"Subject:Hello\n\n{select_quotes}")