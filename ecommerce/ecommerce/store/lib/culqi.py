import requests
import json

class Culqi:

    CHARGE_URL = "https://api.culqi.com/v2/charges"

    def __init__(self, secret):
        self.secret = secret

    def get_headers(self):
        HEADERS = { "Authorization": f"Bearer {self.secret}" }
        return HEADERS

    def create_charge(self, data):
        dumped_data = json.dumps( data )
        response = requests.request("POST", self.__class__.CHARGE_URL, data = dumped_data, headers=self.get_headers())
        return response.json()