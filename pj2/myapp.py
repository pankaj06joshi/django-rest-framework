import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    headers = {'Content-Type': 'application/json'}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data=json_data)
    r_data = r.json()
    print(r_data)    

# get_data(1)

def create_data():
    data = {
        'name': 'avinash',
        'roll': 6,
        'city': 'sikar'
    }
    headers = {'Content-Type': 'application/json'}
    
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    r_data = r.json()
    print(r_data)    

# create_data()

def update_data():
    data = {
        'id': 4,
        'name': 'vikram jain',
        'roll': 4,
        'city': 'kankroli'
    }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    r_data = r.json()
    print(r_data)  

# update_data()

def delete_data():
    data = {'id': 4}
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    r_data = r.json()
    print(r_data) 
    
delete_data()    