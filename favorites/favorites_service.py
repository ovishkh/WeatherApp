import requests
from models.weather_model import Weather
from api.weather_api import API_KEY, WEATHER_URL 


class FavoritesService:
    favorites = []

    @staticmethod
    def add_to_favorites(city):
        if city not in FavoritesService.favorites:
            FavoritesService.favorites.append(city)
            print(f"{city} has been added to your favorites!")
        else:
            print(f"{city} is already in your favorites.")

    @staticmethod
    def show_favorites():
        if FavoritesService.favorites:
            print("\nYour Favorite Cities:")
            for i, city in enumerate(FavoritesService.favorites, start=1):
                print(f"{i}. {city}")
        else:
            print("\nYou have no favorite cities.")

    @staticmethod
    def fetch_favorites_weather():
        if not FavoritesService.favorites:
            print("\nNo favorite cities to fetch weather for.")
            return []

        print("\nFetching weather for your favorite cities...")
        weather_data = []
        for city in FavoritesService.favorites:
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