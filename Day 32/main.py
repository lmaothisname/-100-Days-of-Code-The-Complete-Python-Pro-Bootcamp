##################### Extra Hard Starting Project ######################
import datetime
import pandas
import random
import smtplib
PLACE_HOLDER = "[NAME]"
my_email = "trancaoanhkiet@gmail.com"
password = "lrkb zoks vdpq laxp"
# 1. Update the birthdays.csv
data = pandas.read_csv(r"D:\Python\Day 32\birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now() 
now_tuple = (now.month,now.day)
birthday_person = birthdays_dict[now_tuple]
if now_tuple in birthdays_dict:
    with open(fr"D:\Python\Day 32\letter_templates\letter_{random.randint(1,3)}.txt") as letter_file:
        letter_content = letter_file.read()
        new_letter = letter_content.replace(PLACE_HOLDER,birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg = f"Subject:Happy Birthdays\n\n{new_letter}.")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




