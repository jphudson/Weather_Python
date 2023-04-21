import json

from config import api_key
from connect import *

# jsons from openweathermap
if __name__ == '__main__':
    #city_name = input("Enter city name: ")
    city_name = "New Orleans"

    weather_data = get_weather_data(city_name, api_key)
    forecast_data = get_forecast_data(city_name, api_key)

    if weather_data:
        print(f"Current temperature: {weather_data['main']['temp']}°F")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind speed: {weather_data['wind']['speed']} m/s")
        print(f"Day: {weather_data['']}")

        print("\n")
        print(f"Weather Forecast for tomorrow: ")
        print(f"Day: {forecast_data['list'][0]['dt_txt']}")
        print(f"temp: {forecast_data['list'][0]['main']['temp']}°F")
    else:
        print("Unable to retrieve weather data.")
