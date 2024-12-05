import pandas as pd

class HistoryService:
    history = []  # Store weather history as a list of dictionaries

    @staticmethod
    def add_to_history(city, weather_data): # weather history
        
        HistoryService.history.append({ 
            "City": city,
            "Temperature (°C)": round(weather_data.temp_c, 2),
            "Condition": weather_data.weather,
            "Humidity (%)": weather_data.humidity,
            "Wind Speed (m/s)": weather_data.wind_speed,
            "Timestamp": weather_data.timestamp
        })

    @staticmethod
    def show_history(): # show history
        
        if HistoryService.history:
            print("\nWeather Search History:")
            df = pd.DataFrame(HistoryService.history)
            print(df)
        else:
            print("\nNo history available.")
