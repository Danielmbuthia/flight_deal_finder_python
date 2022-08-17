import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
SHEETY_API = config.get('SHEETY_API')
SHEETY_TOKEN = config.get('SHEETY_TOKEN')

headers = {'Authorization': SHEETY_TOKEN}


class DataManager:
    def fetch_data(self):
        response = requests.get(url=SHEETY_API, headers=headers)
        response.raise_for_status()
        return response.json()['prices']

    def update_data(self, object_id, edit_params):
        response = requests.put(url=f'{SHEETY_API}/{object_id}', json=edit_params, headers=headers)
        response.raise_for_status()
        return response.json()
