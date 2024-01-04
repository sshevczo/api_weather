import requests

class WeatherClient:
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        endpoint = f'{self.base_url}?q={city}&appid={self.api_key}'
        response = requests.get(endpoint)
        return response.json()
    
class WeatherStorageService:
    def __init__(self):
        self.wheather_result = []

    def save_result(self, result):
        self.wheather_result.append(result)

    def get_result(self):
        return self.wheather_result
    
    def delete_result(self, index):
        if 0 <= index < len(self.wheather_result):
            del self.wheather_result[index]
 



if __name__ == '__main__':
    api_key = '1cd6c4ed54ede92936b19e15750a0cb8'

    weather_client = WeatherClient(api_key)
    city_to_check = 'Kharkov'
    weather_result = weather_client.get_weather(city_to_check)
    print('Weather Result:', weather_result)

    storage_service = WeatherStorageService()
    storage_service.save_result(weather_result)
    saved_results = storage_service.get_result()
    print('Saved Results:', saved_results)

    index_to_delete = 0
    storage_service.delete_result(index_to_delete)
    updated_results = storage_service.get_result()
    print('Updated Results:', updated_results)