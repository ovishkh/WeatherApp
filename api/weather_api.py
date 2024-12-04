import requests
from models.weather_model import Weather  # Weather data model

class WeatherAPI:
    """Handles API calls to OpenWeatherMap."""
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = "adb293c2eba52c05f58f2a3148b5bdcb"  # Add your API key here

    def fetch_weather(self, city):
        """Fetch weather data for a city."""
        try:
            url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}"
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                return Weather.from_api_response(data)
            else:
                print(f"Error: {data['message']}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
