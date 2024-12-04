from datetime import datetime

class Weather:
    """Model for weather data."""
    def __init__(self, city, temperature, condition, humidity, wind_speed, timestamp):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.timestamp = timestamp

    @classmethod
    def from_api_response(cls, data):
        """Create a Weather object from API response."""
        city = data["name"]
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        condition = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return cls(city, temp_c, condition, humidity, wind_speed, timestamp)

    def __repr__(self):
        return (
            f"City: {self.city}, Temp: {self.temperature:.2f}°C, "
            f"Condition: {self.condition}, Humidity: {self.humidity}%, "
            f"Wind Speed: {self.wind_speed} m/s, Timestamp: {self.timestamp}"
        )
