import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    r_data = r.json()
    print(r_data)    

# get_data()

def create_data():
    data = {
        'name': 'rankaj',
        'roll': 135,
        'city': 'goa'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    r_data = r.json()
    print(r_data)    

create_data()

def update_data():
    data = {
        'id': 15,
        'name': 'vikram rathor',
        'roll': 122,
        'city': 'lucknow'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    r_data = r.json()
    print(r_data)  

# update_data()

def delete_data():
    data = {'id': 6}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    r_data = r.json()
    print(r_data) 
    
# delete_data()    