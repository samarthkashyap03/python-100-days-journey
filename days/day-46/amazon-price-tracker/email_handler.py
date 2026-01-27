import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv

#Constants
FROM=os.getenv('SENDER_EMAIL')
APP_PASSWORD=os.getenv('APP_PASSWORD')
#Setup Email message
msg=EmailMessage()
msg['From']=FROM
msg['To']=os.getenv('RECIPIENT_EMAIL')
msg['Subject']='Price Drop Alert for your product!'

def send_email(price:float):
    """
    Send an Email to the recipient regarding the price drop
    
    :param price: Enter the new price scraped from the website
    :type price: float
    """
    msg.set_content(f'''
    Hi there!
    Your product is available for a lower price!
    New price:{price}$
    Grab the Deal now!!
    '''
    )
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=FROM,password=APP_PASSWORD)
        try:
            connection.send_message(msg)
        except Exception as e:
            return e
        else:
            return 'Success'


    


