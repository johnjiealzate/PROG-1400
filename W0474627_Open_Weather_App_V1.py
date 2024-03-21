import W0474627_Open_Weather_App
# Enter your API Key
api_key = "7183f487bd1c25233fb7f02cbb25f185"
open_map = W0474627_Open_Weather_App.OpenMapAPI(api_key)
KELVIN = 273.15
# Prompt user for city
city_name = input("Enter city name: ")
city_weather = open_map.get_weather_by_city(city_name)
if city_weather:
    print("Weather in: ", city_name)
    print("Description: ", city_weather['weather'][0]['description'])
    print("Temperature: ", round(KELVIN - city_weather['main']['temp']), "degC")
else:
    print(f"Check City Name, API Key, Network Connection, or if API Service is down.")