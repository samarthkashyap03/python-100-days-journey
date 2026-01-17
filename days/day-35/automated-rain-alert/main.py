import requests,json
from twilio.rest import Client
import os
from dotenv import load_dotenv
#load env variables
load_dotenv() 
WEATHER_API_ENDPOINT=os.getenv('WEATHER_API_ENDPOINT')
auth_token=os.getenv('AUTH_TOKEN')
account_sid=os.getenv('ACCOUNT_SID')
#Constants
parameters={
'appid':'45c2e6a3ab7c61906340dc44f0d8a23c',
'lat':49.444698,
'lon':7.769000,
'units':'metric',
'cnt':4
}

#Twilio Client Setup
client = Client(account_sid, auth_token)

response=requests.get(WEATHER_API_ENDPOINT,params=parameters,timeout=10)
weather_data=response.json()
rain_prediction_data=[data['weather'][0]['main'] for data in weather_data['list']]

def will_it_rain()->bool:
    return any(i=='Rain' for i in rain_prediction_data)

if will_it_rain():
    print('IT will rain')
    message = client.messages.create(
  from_='whatsapp:+14155238886',
  body="Hello Sam, It will rain today. Please carry an umbrella",
  to='whatsapp:+919972730304'
)



