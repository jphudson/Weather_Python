from config import api_key
from connect import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    city_name = input("Enter city name: ")

    weather_data = get_weather_data(city_name, api_key)

    if weather_data:
        print(f"Current temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Unable to retrieve weather data.")