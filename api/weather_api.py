import requests
import pandas as pd
from models.weather_model import Weather
from resources.goods import PREDEFINED_CITIES,WEATHER_TIPS, WEATHER_QUOTES


API_KEY = "adb293c2eba52c05f58f2a3148b5bdcb"  
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"



def fetch_weather_for_country(country):
    cities = PREDEFINED_CITIES.get(country.lower(), [])
    if not cities:
        print(f"No cities found for {country}.")
        return []

    weather_data = []
    for city in cities:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
        }
        try:
            response = requests.get(WEATHER_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather = Weather(data)
                weather_data.append(weather.to_dict())
            else:
                print(f"Error fetching weather for {city}: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching weather for {city}: {e}")

    return weather_data

def display_weather_table(weather_data):
    if weather_data:
        df = pd.DataFrame(weather_data)
        print("\nWeather Information:")
        print(df)
    else:
        print("\nNo weather data available.")