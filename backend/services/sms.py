import json

import requests
from django.http import HttpResponse

from app.settings import SMS_EMAIL, SMS_API_KEY


class SMS:
    uri = f'https://{SMS_EMAIL}:{SMS_API_KEY}@gate.smsaero.ru/v2/'

    def authorize(self):
        uri = self.uri + 'auth'
        result = requests.post(uri)
        return HttpResponse(result)

    def send_sms(self, message, phones):
        url = self.uri + 'sms/send'
        uri = self.get_generated_uri_for_send(message, phones)
        auth = self.authorize()
        text = ''
        split_message = str(message).split(' ')
        for i in range(0, len(split_message)):
            if i != len(split_message) - 1:
                text += split_message[i] + '+'
            else:
                text += split_message[i]
        data = {'numbers': phones, 'text': text, 'sign': 'SMS Aero'}
        if auth.status_code == 200:
            result = requests.get(url, data)
            return HttpResponse(result)

    def get_generated_uri_for_send(self, message, phones):
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
