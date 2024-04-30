import requests
import json
def getAnimalById(id):
    r = requests.get(f'http://127.0.0.1:8000/get-animal?animal_id={id}')
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print('Failed to fetch data:', r.status_code)\
        
def getAllAnimals():
    r = requests.get('http://127.0.0.1:8000/get-all-animals')
    return r.json()
    
def deleteAnimal(id):
    r = requests.delete(f'http://127.0.0.1:8000/delete-animal/{id}')

def createAnimal(id,name,age):
    url = 'http://127.0.0.1:8000/create-animal/{id}?animal_id=%s'%(id)
    print(url) 
    new_data = {'name': name,'age': age}
    

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    r = requests.post(url,headers=headers,json = new_data)

def updateAnimal(id,name,age):
    url = f'http://127.0.0.1:8000/update-animal/{id}' 
    new_data = {'name': name,'age': age}
    print(new_data)

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    r = requests.put(url,headers=headers,json = new_data)