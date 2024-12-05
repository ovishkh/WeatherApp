from datetime import datetime

class Weather:
    def __init__(self, data):
        self.city = data["name"]
        self.temp_k = data["main"]["temp"]
        self.temp_c = self.temp_k - 273.15  # Convert Kelvin to Celsius
        self.weather = data["weather"][0]["description"].capitalize()
        self.humidity = data["main"]["humidity"]
        self.wind_speed = data["wind"]["speed"]
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_weather(self):
        """ Print weather details """
        print("\nWeather Information:")
        print(f"City: {self.city}")
        print(f"Temperature: {self.temp_c:.2f}°C")
        print(f"Condition: {self.weather}")
        print(f"Humidity: {self.humidity}%")
        print(f"Wind Speed: {self.wind_speed} m/s")
        print(f"Timestamp: {self.timestamp}")
