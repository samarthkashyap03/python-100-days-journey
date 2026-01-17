import smtplib,datetime as d,random
import os
from dotenv import load_dotenv
#Load env variables
load_dotenv()
#Constants
SENDER_EMAIL=os.getenv('SENDER_EMAIL')
EMAIL_APP_PASSWORD=os.getenv('EMAIL_APP_PASSWORD')
RECIPIENT_EMAIL=os.getenv('RECIPIENT_EMAIL')
CURRENT_DATE=d.datetime.now()
CURRENT_DAY={
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}
TODAY=CURRENT_DAY[CURRENT_DATE.weekday()]
QUOTES_LIST=[]
#Open the quotes file and load all the quotes to a list
try:
    with open('quotes.txt','r') as f:
        for quote in f:
            QUOTES_LIST.append(quote.strip('\n'))
    random.shuffle(QUOTES_LIST)

except FileNotFoundError:
    print('Quotes.txt not found')
    exit(0)
#Send the email on every wednesdays
if TODAY=='Wednesday':
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL,password=EMAIL_APP_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=RECIPIENT_EMAIL,msg=f"Subject:Daily Motivation\n\n{QUOTES_LIST[0]}")
