from data_objects import Data
from game_data import data as d
def data():
    data_store=[]
    for i in d:
        data=Data(i['name'],i['follower_count'],i['description'],i['country'])
        data_store.append(data)
    return data_store
