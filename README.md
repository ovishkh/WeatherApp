# Weather App
### Your Gateway to Real-Time Weather Information

---

Welcome to the **Weather App** – your ultimate companion for staying updated with the latest weather conditions! 
With features like real-time updates, personalized city management, and insightful weather-based tips, we ensure you're 
always prepared for whatever the skies bring.

---

## Table of content


1. [Introduction](#introduction)  

2. [Features](#features)  

3. [Installation](#installation)   

4. [Usage](#usage)  
  
5. [File Structure](#file-structure)  

6. [API Information](#api-information)  

7. [Dependencies](#dependencies)  

8. [Contribution](#contribution)  

9. [License](#license)
    
10. [Acknowledgements](#acknowledgements)  

---

## Introduction

The Weather App is a simple and user-friendly application designed to provide real-time weather updates. 
You can check the weather for any city or country, save your favorite locations, and view your search history. 
The app also offers helpful weather tips and motivational quotes to enhance your experience.

---


## Features

1. **Real-Time Weather Information**:
   - Fetch weather data for any city or country.
   - Displays temperature, humidity, wind speed, and weather conditions.

2. **Predefined Cities**:
   - Quickly fetch weather for predefined cities in countries like the USA, India, Canada, Australia, and more.

3. **Favorites Management**:
   - Add cities to your favorites list.
   - View and fetch weather for your favorite cities.

4. **Search History**:
   - Keeps track of your weather searches.
   - View your search history in a tabular format.

5. **Weather Tips and Quotes**:
   - Provides helpful tips and motivational quotes based on the current weather conditions.

6. **Developer Information**:
   - Learn about the developers behind the app.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/ApraAditi/Weather-App.git
   cd Weather-App
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

1. **Start the Application**:
   - Run `python app.py` to start the app.

2. **Commands**:
   - `exit`: Quit the application.
   - `history`: View your search history.
   - `favorites`: Manage your favorite cities.
   - `about`: Learn more about the app and its developers.

3. **Search Weather**:
   - Enter a country name to fetch weather for predefined cities in that country.
   - Enter a city name to fetch weather for that specific city.

4. **Favorites Menu**:
   - Option 1: View your favorite cities.
   - Option 2: Add a city to your favorites.
   - Option 3: Fetch weather for all your favorite cities.

---

## File Structure

```
Weather-App/
├── api/
│   ├── __init__.py
│   ├── weather_api.py
├── info/
│   ├── __init__.py
│   ├── info.py
│   ├── requirment.txt
│   ├── concept.txt
├── services/
│   ├── __init__.py
│   ├── history_service.py
├── models/
│   ├── __init__.py
│   ├── weather_model.py
├── favorites/
│   ├── __init__.py
│   ├── favorites_service.py
├── resources/
│   ├── __init__.py
│   ├── goods.py
├── app.py

```

---

## API Information

This app uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch weather data. You need an API key to use this service.

- **API Key**: The app includes a default API key (`adb293c2eba52c05f58f2a3148b5bdcb`). Replace it with your own key if needed.
- **Base URL**: `http://api.openweathermap.org/data/2.5/weather`

---

## Dependencies

The following Python libraries are required:
- `requests`: For making HTTP requests to the weather API.
- `pandas`: For managing and displaying tabular data.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contribution
I welcome contributions to improve the Weather App! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

I would like to express my sincere gratitude to:

* **The OpenWeatherMap team:** For providing the valuable weather data API that powers this application.
* **The Python community:** For developing and maintaining the Python programming language and its extensive libraries.

--- 

Enjoy using the Weather App! Stay informed and prepared for any weather conditions. 🌤️
