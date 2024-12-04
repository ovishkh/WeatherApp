from api.weather_api import WeatherAPI  # API module
from services.history_service import HistoryService  # History module
from models.weather_model import Weather  # Data model

class WeatherApp:
    """Main Weather App class implementing OOP concepts."""
    def __init__(self):
        self.api = WeatherAPI()  # API interaction
        self.history_service = HistoryService()  # Manage search history

    def display_weather(self, weather):
        """Display weather details for the user."""
        print("\nWeather Information:")
        print(f"City: {weather.city}")
        print(f"Temperature: {weather.temperature:.2f}°C")
        print(f"Condition: {weather.condition}")
        print(f"Humidity: {weather.humidity}%")
        print(f"Wind Speed: {weather.wind_speed} m/s")
        print(f"Timestamp: {weather.timestamp}")

    def show_history(self):
        """Show history of weather searches."""
        history = self.history_service.get_history()
        if history:
            print("\nWeather Search History:")
            for record in history:
                print(record)
        else:
            print("\nNo history available.")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Weather App!")
        print("Type 'exit' to quit the application.")
        print("Type 'history' to view your search history.\n")

        while True:
            city = input("Enter city name: ").strip()
            if city.lower() == "exit":
                print("Goodbye!")
                break
            elif city.lower() == "history":
                self.show_history()
            else:
                weather_data = self.api.fetch_weather(city)
                if weather_data:
                    self.history_service.add_to_history(weather_data)
                    self.display_weather(weather_data)

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
