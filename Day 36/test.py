import requests
from datetime import date,timedelta
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK_KEY = "BUS0TI91V2HP3PTE"
NEWS_API_KEY = "23e9c5b98d1647478fbd991647ee2637"
account_sid = "AC94e9f7636b23d5bc94a32c4384bf30e7"
auth_token = "838ab690dfd31182b471b21b1a187473"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : API_STOCK_KEY,
}
response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
data = response.json()
print(data)
# now = date.today()
# yesterday = now - timedelta(days=2)
# day_before_yesterday = now - timedelta(days=3)
# stock_yesterday = data["Time Series (Daily)"][str(yesterday)]["4. close"]
# stock_day_before_yesterday = data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
# change_stock = round(((float(stock_yesterday) - float(stock_day_before_yesterday)) / float(stock_day_before_yesterday)) * 100,2)