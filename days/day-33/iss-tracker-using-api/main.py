import requests
import smtplib
from email.message import EmailMessage
import datetime as d
import clipboard
import os
from dotenv import load_dotenv

#load env variables
load_dotenv()

#Constants
MY_LATITUDE=49.430455
MY_LONGITUDE=7.774098
CURRENT_TIME=d.datetime.now()
CURRENT_HOUR=int(CURRENT_TIME.strftime("%H"))
CURRENT_MINUTE=int(CURRENT_TIME.strftime("%M"))
SENDER_EMAIL=os.getenv('SENDER_EMAIL')
EMAIL_APP_PASSWORD=os.getenv('EMAIL_APP_PASSWORD')
RECIPIENT_EMAIL=os.getenv('RECIPIENT_EMAIL')

#Email Client Setup
msg=EmailMessage()
msg['From']=SENDER_EMAIL
msg['To']=RECIPIENT_EMAIL
msg['Subject']='Please Look above'
msg.set_content('''
Hi Samarth, 
The ISS has come to your Location and its dark, Please look above the skies and enjoy!''')

#Connect to API
try:
    iss_data=requests.get(url='http://api.open-notify.org/iss-now.json',timeout=10).json()
    sunrise_sunset_data=requests.get(url='https://api.sunrise-sunset.org/json',params={'lat':MY_LATITUDE,'lng':MY_LONGITUDE,'formatted':0},timeout=10).json()
except:
    print("Error Connecting to API")
    exit(0)

#Fetch data from API response and format it
lattitude=iss_data['iss_position']['latitude']
longitude=iss_data['iss_position']['longitude']
sunrise_time=sunrise_sunset_data['results']['sunrise'].split('T')[1].split(':')
sunset_time=sunrise_sunset_data['results']['sunset'].split('T')[1].split(':')
now_minutes=CURRENT_HOUR*60+CURRENT_MINUTE
sunrise_minutes=int(sunrise_time[0]*60+sunrise_time[1])
sunset_minutes=int(sunset_time[0]*60+sunset_time[1])

#Functions
def check_position():
    return (MY_LATITUDE-5<=float(lattitude)<=MY_LATITUDE+5) and (MY_LONGITUDE-5<=float(longitude)<=MY_LONGITUDE+5)
def check_time():
    return (now_minutes>=sunset_minutes or now_minutes<=sunrise_minutes)
def send_mail():
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL,password=EMAIL_APP_PASSWORD)
            connection.send_message(msg)

#Main Logic
if check_position():
    if check_time():
         send_mail()
        
        


