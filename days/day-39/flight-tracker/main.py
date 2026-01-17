import os
from dotenv import load_dotenv
import requests

load_dotenv()
SHEETY_HEADER={
    'Authorization':f"Bearer {os.getenv('AUTHORISATION_TOKEN')}",
    'Content-Type':'application/json'
}
#Step-1: retrieve the sheets data and populate with city codes
data=requests.get(url=os.getenv('SHEET_GET_ENDPOINT'),headers=SHEETY_HEADER).json()
row_number=2
for i in data['tracker']:
    city=i['city'].upper()
    iata_code=requests.get(url=os.getenv('FLIGHT_CITY_SEARCH_ENDPOINT'),params={'keyword':city},headers={'Authorization':f"Bearer {os.getenv('ACCESS_TOKEN')}"}).json()
    iata_code=iata_code['data'][0].get('iataCode')
    data={'tracker':{'cityCode':iata_code}}
    response=requests.put(url=f"{os.getenv('SHEET_POST_ENDPOINT')}/{row_number}",headers=SHEETY_HEADER,json=data)
    row_number+=1
    print(response.status_code)
    response=requests.get()
  
    
