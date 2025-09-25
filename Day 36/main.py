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
now = date.today()
yesterday = now - timedelta(days=2)
day_before_yesterday = now - timedelta(days=3)
stock_yesterday = data["Time Series (Daily)"][str(yesterday)]["4. close"]
stock_day_before_yesterday = data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
difference = float(stock_yesterday) - float(stock_day_before_yesterday)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference/float(stock_day_before_yesterday)) * 100,2)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(diff_percent) >= 5:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    new_response = requests.get(url="https://newsapi.org/v2/everything",params=news_params)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid,auth_token)
    for article in formatted_articles:
        message = client.messages.create(
        from_="+1251333158936",
        body=article,
        to="+1415523888618"
        )
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

