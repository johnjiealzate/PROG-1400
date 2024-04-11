import W0474627_PROG1400_Open_Weather_App
# Enter your API Key
api_key = "7183f487bd1c25233fb7f02cbb25f185"
open_map = W0474627_PROG1400_Open_Weather_App.OpenMapAPI(api_key)
KELVIN = 273.15
# Prompt user for city
city_name = input("Enter city name: ")

# Error handling
try:
    city_weather = open_map.get_weather_by_city(city_name)
    print(city_weather)
except NameError:
    print(f"API Connection Error")

if city_weather:
    if city_weather['cod'] == 200:
        print("Weather in: ", city_name)
        # Print("At time", datetime(city_weather['dt]))
        print("Description: ", city_weather['weather'][0]['description'])
        print("Temperature: ", round(city_weather['main']['temp'] - KELVIN), "°C")
        print("Feels like: ", round(city_weather['main']['feels_like'] - KELVIN), "°C")
        print("Humidity: ", city_weather['main']['humidity'], "%")
        print("Wind Speed: ", city_weather['wind']['speed'], "km/h")
    else:
        print(f"Error COde: {city_weather['cod']}")
        print(f"Error Message: {city_weather['message'].capitalize()}")