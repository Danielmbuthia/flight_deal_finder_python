import requests
from dotenv import dotenv_values

config = dotenv_values('.env')

FLIGHT_URL = 'https://tequila-api.kiwi.com/'
TEQUILA_API_KEY = config.get('TEQUILA_API_KEY')


class FlightSearch:
    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f'{FLIGHT_URL}locations/query', params=query, headers=headers)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
