from api.weather_api import fetch_weather, display_weather
from info.info import DevInfo
from services.history_service import HistoryService

app_info = DevInfo() # Initialize the concrete class for app info

history_service = HistoryService() # Initialize the history service

def main():

    app_info.show_app_info()  # Show app details

    print("\nType 'exit' to quit the application.")
    print("Type 'history' to view your search history.")
    print("Type 'about' to know more about the app.\n")

    while True:
        city = input("Enter city name: ").strip()

        if city.lower() == "exit":
            print("Goodbye!")
            break
        elif city.lower() == "history":
            history_service.show_history()  # Show history
        elif city.lower() == "about":
            app_info.show_developer_info()  # Show developer info
        else:
            weather_data = fetch_weather(city)
            if weather_data:
                display_weather(weather_data)
                history_service.add_to_history(city, weather_data)  # Add to history

if __name__ == "__main__":
    main()
