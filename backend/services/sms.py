import json

import requests
from django.http import HttpResponse

from app.settings import SMS_EMAIL, SMS_API_KEY


class SMSService:
    uri = f'https://{SMS_EMAIL}:{SMS_API_KEY}@gate.smsaero.ru/v2/'

    def authorize(self):
        uri = self.uri + 'auth'
        result = requests.post(uri)
        return HttpResponse(result)

    def send_sms(self, message, phones):
        uri = self.__get_generated_uri_for_send(message, phones)
        auth = self.authorize()

        if auth.status_code == 200:
            response = requests.get(uri)
            return HttpResponse(response)

    def __get_generated_uri_for_send(self, message, phones) -> str:
        uri = self.uri + 'sms/send?'
        for phone in phones:
            uri += f'numbers[]={phone}&'
        uri += f'text='

        split_message = str(message).split(' ')
        for i in range(0, len(split_message)):
            if i != len(split_message) - 1:
                uri += split_message[i] + '+'
            else:
                uri += split_message[i]
        uri = uri[0:-1] + f'&sign=SMS Aero'
        return uri

    def get_current_balance(self) -> float:
        uri = self.uri + 'balance'
        auth = self.authorize()

        if auth.status_code == 200:
            response = requests.get(uri)
            return float(response.json()['data']['balance'])
