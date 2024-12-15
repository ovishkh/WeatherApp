from datetime import datetime, timedelta
from resources.goods import PREDEFINED_CITIES,WEATHER_TIPS, WEATHER_QUOTES


class Weather:
    def __init__(self, data):
        self.city = data["name"]
        self.temp_c = data["main"]["temp"]
        self.temp_max_c = data["main"]["temp_max"]
        self.temp_min_c = data["main"]["temp_min"]
        self.weather = data["weather"][0]["description"].lower()
        self.humidity = data["main"].get("humidity", "N/A")
        self.wind_speed = data["wind"].get("speed", "N/A")
        self.stream = "Normal" if self.temp_c < 35 else "Overheating"
        self.heatwave = "Yes" if self.temp_c > 40 else "No"
        self.snowfall = "Yes" if "snow" in self.weather or self.temp_c <= 0 else "No"

        utc_time = datetime.utcnow()
        timezone_offset = data.get("timezone", 0)
        local_time = utc_time + timedelta(seconds=timezone_offset)
        self.timestamp = local_time.strftime("%Y-%m-%d %H:%M:%S")

        self.tip = self.get_weather_tip()
        self.quote = self.get_weather_quote()

    def get_weather_tip(self):
        if "snow" in self.weather or self.snowfall == "Yes":
            return WEATHER_TIPS["snow"][0]
        elif "rain" in self.weather:
            return WEATHER_TIPS["rain"][0]
        elif "thunderstorm" in self.weather:
            return WEATHER_TIPS["thunderstorm"][0]
        elif "mist" in self.weather or "fog" in self.weather:
            return WEATHER_TIPS["mist"][0]
        elif "clear" in self.weather:
            return WEATHER_TIPS["clear"][0]
        elif "clouds" in self.weather:
            return WEATHER_TIPS["clouds"][0]
        else:
            return WEATHER_TIPS["default"][0]

    def get_weather_quote(self):
        if "snow" in self.weather or self.snowfall == "Yes":
            return WEATHER_QUOTES["snow"][0]
        elif "rain" in self.weather:
            return WEATHER_QUOTES["rain"][0]
        elif "thunderstorm" in self.weather:
            return WEATHER_QUOTES["thunderstorm"][0]
        elif "mist" in self.weather or "fog" in self.weather:
            return WEATHER_QUOTES["mist"][0]
        elif "clear" in self.weather:
            return WEATHER_QUOTES["clear"][0]
        elif "clouds" in self.weather:
            return WEATHER_QUOTES["clouds"][0]
        else:
            return WEATHER_QUOTES["default"][0]


    def to_dict(self):
        return {
            "City": self.city,
            "Temperature (°C)": round(self.temp_c, 2),
            "Max Temperature (°C)": round(self.temp_max_c, 2),
            "Min Temperature (°C)": round(self.temp_min_c, 2),
            "Condition": self.weather.capitalize(),
            "Humidity (%)": self.humidity,
            "Wind Speed (m/s)": self.wind_speed,
            "Stream": self.stream,
            "Heatwave": self.heatwave,
            "Snowfall": self.snowfall,
            "Timestamp": self.timestamp,
        }

    def display_single_city_weather(self):
        print("\nWeather Information:")
        print(f"City: {self.city}")
        print(f"Temperature: {self.temp_c}°C")
        print(f"Max Temperature: {self.temp_max_c}°C")
        print(f"Min Temperature: {self.temp_min_c}°C")
        print(f"Condition: {self.weather.capitalize()}")
        print(f"Humidity: {self.humidity}%")
        print(f"Wind Speed: {self.wind_speed} m/s")
        print(f"Stream: {self.stream}")
        print(f"Heatwave: {self.heatwave}")
        print(f"Snowfall: {self.snowfall}")
        print(f"Timestamp: {self.timestamp}")
        print(f"\nTip: {self.tip}")
        print(f"Quote: {self.quote}")