import os
from dotenv import load_dotenv
import requests,json
import datetime as dt
from groq import Groq
#Load theenv variables
load_dotenv()
date=dt.datetime.now()
TOKEN=os.getenv('TOKEN')
HEADER={
    "Authorization":f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}
#Setup Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)
#Define API Endpoints
GET_ENDPOINT=os.getenv('SHEETY_GET_ENDPOINT')
POST_ENDPOINT=os.getenv('SHEETY_POST_ENDPOINT')


def read_sheet_data():
    try:
        sheet_data=requests.get(url=GET_ENDPOINT,headers=HEADER,timeout=10).json()
        return sheet_data
    except requests.exceptions.RequestException as e:
        print(f'Exception Occured: {e}')



def post_data(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":prompt,
            }
        ],
        model="llama-3.3-70b-versatile",# or any other available model
    )
    data=json.loads(chat_completion.choices[0].message.content)
    try:
        response=requests.post(url=POST_ENDPOINT,headers=HEADER,json=data)
        print('Success')
        return response.status_code
    except requests.exceptions.RequestException:
        print("Error occured, Try again")
        return response.status_code
    
def generate_prompt(user_input):
    prompt=f""" You are a JSON formatter.
                Given a user's workout description, extract:
                - exercise (string), identify what exercise it is and output is verb+ing form of it like running, walking etc
                - duration (string, but just a numerical value followed by mins or hours, as specified by user, if its more than 60 mins denote in hours like 1 hour)
                - calories (number, approximate calories burned for that activity and duration)
                Rules:
                - Output MUST be valid JSON
                - Output ONLY the JSON object
                - Do NOT add explanations, comments, markdown, or extra text
                - Do NOT wrap the JSON in code blocks
                - If any field is missing, make a reasonable assumption
                Input: {user_input}
                Output format:
                'workout':{{
                {{
                "date":"{date.date().strftime('%d-%m-%Y')}"
                'time':{date.time().strftime('%H:%M:%S')} formatted properly in 12 hr format, with am or pm ,
                "exercise": "",
                "duration": "",
                "calories": 0
                }}}}"""
    return prompt

def write_log(response):
    try:
        with open('log.json','a') as f:
            data={date.time().strftime('%H:%M:%S'):{'Status code':response,'operation':'POST'}}
            json.dump(data,f,indent=4)
    except FileNotFoundError:
        with open('json.txt','w') as f:
            data={date.time().strftime('%H:%M:%S'):{'Status code':response,'operation':'POST'}}
            json.dump(data,f,indent=4)
def main():
    user_input=input('Please describe your activity, what you did today!')
    prompt=generate_prompt(user_input)
    response=post_data(prompt)
    write_log(response)

main()
