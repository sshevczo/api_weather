import requests
from typing import List, Dict, Any

class OpenWeatherMapClient:
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_weather(self, city: str) -> Dict[str, Any]:
        endpoint = f'{self.base_url}?q={city}&appid={self.api_key}'
        response = requests.get(endpoint)
        return response.json()

class WeatherStorageService:
    def __init__(self) -> None:
        self.weather_results: List[Dict[str, Any]] = []

    def save_result(self, result: Dict[str, Any]) -> None:
        self.weather_results.append(result)

    def get_results(self) -> List[Dict[str, Any]]:
        return self.weather_results

    def delete_result(self, index: int) -> None:
        if 0 <= index < len(self.weather_results):
            del self.weather_results[index]

if __name__ == '__main__':
    api_key = '1cd6c4ed54ede92936b19e15750a0cb8'

    weather_client = OpenWeatherMapClient(api_key)
    city_to_check = 'Kharkiv'
    weather_result = weather_client.get_weather(city_to_check)
    print('Weather Result:', weather_result)

    storage_service = WeatherStorageService()
    storage_service.save_result(weather_result)
    saved_results = storage_service.get_results()
    print('Saved Results:', saved_results)

    index_to_delete = 0
    storage_service.delete_result(index_to_delete)
    updated_results = storage_service.get_results()
    print('Updated Results:', updated_results)
