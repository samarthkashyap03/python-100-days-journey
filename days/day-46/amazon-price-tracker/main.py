#This project tracks the price of a product on Amazon and notifies the user when the price drops below a specified threshold.
from amazon import scrape_data
from email_handler import send_email

TARGET_PRICE=100 #Change as per your target price
URL="ENTER THE URL OF THE AMAZON PRODUCT YOU WANT TO TRACK"

def main():
    current_price=scrape_data(URL)
    if current_price<TARGET_PRICE:
        print(send_email(current_price))
main()
