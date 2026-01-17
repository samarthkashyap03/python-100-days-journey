import requests,os,create_graph,datetime as d
from dotenv import load_dotenv
date=d.datetime.now().strftime('%Y%m%d')
load_dotenv()
HEADERS={
        'X-USER-TOKEN':os.getenv('PIXELA_TOKEN')
    }
def create_pixel():
    API_ENDPOINT=f"https://pixe.la/v1/users/{create_graph.USERNAME}/graphs/test-graph"
    API_PARAMS={
        "date":date,
        "quantity":"5",
        }
    response=requests.post(url=API_ENDPOINT,json=API_PARAMS,headers=HEADERS,timeout=10)
    print(response.text)

def update_pixel(update_value:str):
    API_ENDPOINT=f"https://pixe.la/v1/users/{create_graph.USERNAME}/graphs/test-graph/{date}"
    params={
        'quantity':str(update_value)
    }
    response=requests.put(url=API_ENDPOINT,headers=HEADERS,json=params)
    print(response.text)

def delete_pixel():
    API_ENDPOINT=f"https://pixe.la/v1/users/{create_graph.USERNAME}/graphs/test-graph/{date}"
    response=requests.delete(url=API_ENDPOINT,headers=HEADERS)
    print(response.text)

"""create_pixel()
update_pixel(15)
delete_pixel()"""