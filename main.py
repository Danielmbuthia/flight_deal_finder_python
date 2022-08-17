from data_manager import DataManager
from pprint import pprint

from flight_search import FlightSearch

data_manager = DataManager()
sheety_data = data_manager.fetch_data()

flight_search = FlightSearch()
sheety_data_dict = {row.get('city'): row.get('id') for row in sheety_data if row.get('iataCode') == ""}

if len(sheety_data_dict) > 0:
    for key, value in sheety_data_dict.items():
        city_name = flight_search.get_destination_code(key)
        edit_params = {
            'price': {
                'iataCode': city_name
            }
        }
        response = data_manager.update_data(object_id=value, edit_params=edit_params)
        pprint(response)
