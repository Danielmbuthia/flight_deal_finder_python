from dotenv import dotenv_values
from twilio.rest import Client

config = dotenv_values('.env')

TWILIO_SID = config.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = config.get('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = config.get('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = config.get('TWILIO_VERIFIED_NUMBER')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
