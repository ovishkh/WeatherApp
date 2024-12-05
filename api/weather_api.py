import requests
from models.weather_model import Weather

API_KEY = "adb293c2eba52c05f58f2a3148b5bdcb"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city): #  Fetch weather data from the OpenWeatherMap API.

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:  # Successful response
            # Return a Weather object
            return Weather(data)
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    
    weather_data.display_weather() # Display the weather data.
