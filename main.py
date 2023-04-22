import json

from config import api_key
from connect import *
from datetime import date

# jsons from openweathermap
if __name__ == '__main__':
    #city_name = input("Enter city name: ")
    city_name = "New Orleans"

    weather_data = get_weather_data(city_name, api_key)
    forecast_data = get_forecast_data(city_name, api_key)
    print(json.dumps(weather_data, indent=2))
    print(json.dumps(forecast_data, indent=2))

    if weather_data:
        print(f"Weather Data for New Orleans Today {date.today().strftime('%m/%d/%y')}:")
        print(f"Current temperature: {weather_data['main']['temp']}°F")
        print(f"Feels Like: {weather_data['main']['feels_like']}°F")
        print(f"Low: {weather_data['main']['temp_min']}°F")
        print(f"High: {weather_data['main']['temp_max']}°F")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind speed: {weather_data['wind']['speed']} mph")
        print(f"Weather Description: {weather_data['weather'][0]['description']}")

        print("\n")
        print(f"Weather Forecast for tomorrow: ")
        print(f"Day: {forecast_data['list'][0]['dt_txt']}")
        print(f"temp: {forecast_data['list'][0]['main']['temp']}°F")
    else:
        print("Unable to retrieve weather data.")
