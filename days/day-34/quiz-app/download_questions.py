import requests,json
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_TRIVIA_ENDPOINT=os.getenv('OPEN_TRIVIA_ENDPOINT')

def download_questions()->None:
    """Downloads questions using OpenTrivia API and stores it in questions.json"""
    response=requests.get(url=OPEN_TRIVIA_ENDPOINT,timeout=10)
    with open('questions.json','w') as f:
        json.dump(response.json(),f)