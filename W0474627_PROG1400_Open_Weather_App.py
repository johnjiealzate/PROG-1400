import requests
import json

class OpenMapAPI:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.message = ""

    def get_weather_by_city(self, city_name):
        # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        url = f"{self.base_url}?q={city_name}&appid={self.api_key}"
        # Error checking
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except:
            print("Error connecting to API Service")
