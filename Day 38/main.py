import requests
from datetime import datetime
import os
APP_ID = "18a91ad7b036"
API_KEY = "75cbb8a1932fcd0ad4b0c8d17c38c6ec2b43"
GENDER = "male"
WEIGHT = 100
HEIGHT = 183
AGE = 19
USERNAME = "lmaothiscoach"
PASSWORD = "tenbopkiet"
natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
sentence = input("Tell me which excercise you did:")
parameters = {
    "query" : sentence,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE,
}
response = requests.post(url=natural_language_endpoint,json=parameters,headers=headers)
result = response.json()

sheety_endpoint = "https://api.sheety.co/5639f710feafa0087dc520e69971d129/workoutTracking/workouts"
today_date = datetime.now().strftime(r"%d/%m/%y")
now_time = datetime.now().strftime(r"%X")

for excercise in result["exercises"]:
    sheet_input = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "excercise" : excercise["name"].title(),
            "duration" : excercise["duration_min"],
            "calories" : excercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheety_endpoint,json=sheet_input,auth=(USERNAME,PASSWORD))
    print(sheet_response.text)