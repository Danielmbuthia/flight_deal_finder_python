from datetime import datetime, timedelta

from notification_manager import NotificationManager
from data_manager import DataManager
from pprint import pprint

from flight_search import FlightSearch

ORIGIN_CITY_IATA = 'NBO'

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


sheety_data = data_manager.fetch_data()
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

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheety_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    pprint(flight)
    pprint(destination)
    if flight:
        print(flight.price)
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )

