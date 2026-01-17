import requests
from dotenv import load_dotenv
import os,datetime as d
date=d.datetime.now().date()
from itertools import islice
from twilio.rest import Client

load_dotenv()
#load env variables
STOCK_API_KEY=os.getenv('STOCK_API_KEY')
NEWS_API_KEY=os.getenv('NEWS_API_KEY')
auth_token = os.getenv('AUTH_TOKEN')
account_sid=os.getenv('ACCOUNT_SID')
SENDER_PHONE_NUMBER=os.getenv('CALLER_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER=os.getenv('RECIPIENT_PHONE_NUMBER')
STOCK=os.getenv('STOCK_SYMBOL')
COMPANY_NAME=os.getenv('COMPANY_NAME')
#Twilio Client Setup
client = Client(account_sid, auth_token)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_data()->str:
    stock_api_get=requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={os.getenv('STOCK_API_KEY')}",timeout=10)
    stock_data=dict(islice(stock_api_get.json()['Time Series (Daily)'].items(),2))
    difference=round(float(stock_data[list(stock_data.keys())[0]]['1. open'])-float(stock_data[list(stock_data.keys())[1]]['4. close']),2)
    percentage_change=round((float(stock_data[list(stock_data.keys())[1]]['1. open'])/float(stock_data[list(stock_data.keys())[0]]['4. close'])-1)*100,2)
    if difference<0:
        return f"{COMPANY_NAME} Price has Dropped by: ${round(difference,2)*-1}, CHANGE%: {round(percentage_change,2)}%"
    else:
        return f"{COMPANY_NAME} Price has Increased by: ${round(difference,2)}, CHANGE%: {round(percentage_change,2)}%"
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news()->list:
    news_api=requests.get(f"https://newsapi.org/v2/everything?apiKey={os.getenv('NEWS_API_KEY')}&q={COMPANY_NAME}&pageSize=50&sortBy=relevancy")
    headlines=list(i['title'] for i in news_api.json()['articles'])[:3]
    return headlines

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_stock_info():
    message = client.messages.create(
    from_=f'whatsapp:{SENDER_PHONE_NUMBER}',
    body=get_stock_data(),
    to=f'whatsapp:{RECIPIENT_PHONE_NUMBER}'
)
def send_news():
    for i in get_news():
        message = client.messages.create(
        from_=f'whatsapp:{SENDER_PHONE_NUMBER}',
        body=f"ARTICLE: {i}\n",
        to=f'whatsapp:{RECIPIENT_PHONE_NUMBER}'
)
    
send_stock_info()
send_news()

