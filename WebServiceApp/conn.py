import requests
import json

link = 'https://simple-codi-dimaldinho.koyeb.app/'


def getAnimalById(id):
    retrive_data_from_api = requests.get(f'{link}get-animal?animal_id={id}')
    
    if retrive_data_from_api.status_code == 200:
        return retrive_data_from_api.json()
    else:
        print('Failed to fetch data:', retrive_data_from_api.status_code)


def getAllAnimals():
    retrive_data_from_api = requests.get(f'{link}get-all-animals')
    return retrive_data_from_api.json()


def createAnimal(name,age):
    url = '%screate-animal/{}?animal_name=%s&animal_age=%s'%(link,name,age)
    #print(url)
    new_data = {'name': name,'age': age}

    requests.post(url,json = new_data)
    

def updateAnimal(id,name,age):
    url = f'{link}update-animal/{id}?animal_name={name}&animal_age={age}'
    new_data = {'name': name,'age': age}
    
    requests.put(url,json = new_data)


def deleteAnimal(id):
    requests.delete(f'{link}delete-animal/{id}')