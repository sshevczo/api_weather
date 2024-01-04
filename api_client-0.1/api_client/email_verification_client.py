import requests

class EmailVerificationClient:
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key):
        self.api_key = api_key

    def verify_email(self, email):
        endpoint = f'{self.base_url}/verify'
        params = {'email': email, 'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        return response.json()
