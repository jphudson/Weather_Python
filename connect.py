import requests


def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_forecast_data(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast/?q={city_name}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
