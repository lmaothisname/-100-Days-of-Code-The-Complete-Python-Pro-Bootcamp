import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5639f710feafa0087dc520e69971d129/flightDealsUser/prices"
class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.authorization = HTTPBasicAuth(self._user,self._password)
        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",json=new_data,auth=self.authorization)
            print(response.text)
        