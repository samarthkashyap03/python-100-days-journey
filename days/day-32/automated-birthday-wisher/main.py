from email.message import EmailMessage
import smtplib
import pandas as pd
import datetime as d
import os
from dotenv import load_dotenv
load_dotenv()
THIS_DAY=d.datetime.now().day
THIS_MONTH=d.datetime.now().month
SENDER_EMAIL=os.getenv('SENDER_EMAIL')
APP_PASSWORD=os.getenv('EMAIL_APP_PASSWORD')

try:
    BIRTHDAY_DATA=pd.read_csv('birthdays.csv')
except FileNotFoundError:
    print("Please load the file birthdays.csv")
    exit(0)

msg=EmailMessage()
msg['From']=SENDER_EMAIL
msg['Subject']='Happy Birthday'

def format_message(name:str):
    msg.set_content(f"""
Happy Birthday {name}! 🎂

Wishing you a fantastic day filled with joy, laughter, and wonderful memories.

Celebrate big and enjoy every moment!

— Your Friends at YourApp
                    """)
    
def format_html(name:str):
    msg.add_alternative(f"""
<!DOCTYPE html>
<html>
  <body style="margin:0; padding:0; background-color:#f0f4f8; font-family:Arial, sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td align="center" style="padding:40px 0;">

          <!-- Confetti Header -->
          <div style="font-size:32px; text-align:center; line-height:1.2; padding-bottom:20px;">
            🎉🎈🎁🎊🎂🎉🎈🎁🎊🎂🎉
          </div>

          <!-- Card -->
          <table width="100%" style="max-width:600px; background:#ffffff; border-radius:12px; padding:30px; box-shadow:0 4px 20px rgba(0,0,0,0.1);">
            
            <!-- Header -->
            <tr>
              <td align="center" style="font-size:28px; font-weight:bold; color:#ff6f61; padding-bottom:20px;">
                🎉 Happy Birthday {name}! 🎉
              </td>
            </tr>
            
            <!-- Message -->
            <tr>
              <td style="font-size:16px; color:#333333; line-height:1.6; text-align:center; padding-bottom:20px;">
                Wishing you a fantastic day filled with joy, laughter, and wonderful memories. May all your dreams come true this year!
              </td>
            </tr>
            
            <!-- Image -->
            <tr>
              <td align="center" style="padding-bottom:20px;">
                <img src="https://files.123freevectors.com/wp-content/original/517668-happy-birthday-glitter-greeting-card-burgundy-and-gold.webp" 
                     alt="Birthday Cake" width="150" style="border-radius:12px;">
              </td>
            </tr>
            
            <!-- Button -->
            <tr>
              <td align="center" style="padding-bottom:20px;">
                <a href="https://bdaycake.com/samarthkashyap_4234?invitation_code=HPRJ" 
                   style="background:#ff6f61; color:#ffffff; text-decoration:none;
                          padding:12px 28px; border-radius:8px; font-size:16px; display:inline-block;">
                  Celebrate Now 🎈
                </a>
              </td>
            </tr>
            
            <!-- Footer with mini confetti -->
            <tr>
              <td style="font-size:12px; color:#777777; text-align:center; border-top:1px solid #eee; padding-top:16px;">
                Have a wonderful year ahead! 🎉🎁🎈<br>
                Yours Truly,<br>
                Samarth
              </td>
            </tr>

          </table>

          <!-- Confetti Footer -->
          <div style="font-size:28px; text-align:center; line-height:1.2; padding-top:20px;">
            🎊🎁🎈🎉🎂🎊🎁🎈🎉🎂
          </div>

        </td>
      </tr>
    </table>
  </body>
</html>
""",subtype='html')
    
for index,data in BIRTHDAY_DATA.iterrows():
    if THIS_MONTH==data['month'] and THIS_DAY==data['day']:
        name=data['name']
        msg['To']=str(data['email'])
        format_message(name)
        format_html(name)
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL,password=APP_PASSWORD)
            connection.send_message(msg)
        print(data['name'])


