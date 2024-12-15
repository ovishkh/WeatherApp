import pandas as pd

class HistoryService:
    history = []

    @staticmethod
    def add_to_history(weather_data):
        HistoryService.history.append(weather_data)

    @staticmethod
    def show_history():
        if HistoryService.history:
            print("\nWeather Search History:")
            df = pd.DataFrame(HistoryService.history)
            print(df)
        else:
            print("\nNo history available.")
