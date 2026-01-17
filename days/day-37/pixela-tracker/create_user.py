import requests,os
from dotenv import load_dotenv
load_dotenv()
def create_user(username:str)->str:
    """Creates a user with 'username', returns the response text."""
    API_ENDPOINT="https://pixe.la/v1/users"
    API_PARMS={
        "token":os.getenv('PIXELA-TOKEN'),
        "username":os.getenv('PIXELA_USERNAME'), 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes"
    }
    response=requests.post(url=API_ENDPOINT,json=API_PARMS,timeout=10)
    return response.text

