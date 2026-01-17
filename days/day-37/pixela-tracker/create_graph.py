import os,requests
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('PIXELA_TOKEN')
USERNAME=os.getenv('PIXELA_USERNAME')
def create_graphs()->str:
    API_PARAMS={
        "id":"test-graph",
        "name":"Coding_graph",
        "unit":"commit",
        "type":"int",
        "color":"shibafu",
        "timezone":"Europe/Berlin",
    }
    HEADERS={
        'X-USER-TOKEN':TOKEN
    }
    response=requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs',json=API_PARAMS,headers=HEADERS)
    return response.text