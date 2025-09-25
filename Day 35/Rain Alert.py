import requests
from twilio.rest import Client
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "982447f780737b8858afe0163cb04aaf"
account_sid = "AC94e9f7636b23d5bc94a32c4384bf30e7"
auth_token = "838ab690dfd31182b471b21b1a187473"
parameters = {
    "lat": 51.759048,
    "lon": 19.458599,
    "appid": api_key,
    "cnt" : 4,
}
response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
data = response.json()
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_="whatsapp:+12513331589",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+14155238886"
    )
    print(message.status)