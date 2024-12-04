# WeatherApp

## Your Gateway to Real-Time Weather Information

Welcome to **WeatherApp**, a Python-based command-line application that fetches real-time weather data for any city around the world. This repository contains the code and resources for building a simple yet professional weather application that allows users to access weather information using the OpenWeatherMap API.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Introduction

WeatherApp is a Python-based command-line application that allows users to search for current weather information by entering a city name. It uses the OpenWeatherMap API to fetch real-time data, and the results are displayed in a clean and user-friendly format. This app is built with object-oriented principles, including abstraction, encapsulation, and polymorphism, and supports a historical search feature.

---

## Features

- Real-time weather information (temperature, humidity, wind speed, etc.)
- Search history tracking
- Interactive command-line interface
- Easy-to-use and lightweight
- Built using object-oriented programming concepts (OOP)
- Uses OpenWeatherMap API for weather data

---

## Technologies Used

- **Backend**: Python 3.x
- **Libraries**: `requests`, `pandas`, `json`, `datetime`
- **API**: OpenWeatherMap API (Weather data)

---

## Installation

To get a copy of the WeatherApp running on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ovishkh/WeatherApp.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd WeatherApp
    ```

3. **Install dependencies:**
    You can use `pip` to install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - You'll need an **OpenWeatherMap API Key**. You can obtain it from [OpenWeatherMap](https://openweathermap.org/api).
    - Create a `.env` file in the root directory and add your API key:
      ```bash
      API_KEY="your_api_key_here"
      ```

5. **Run the application:**
    ```bash
    python app.py
    ```

---

## Usage

Once the application is running, simply enter the city name when prompted to receive the weather details. You can also check the weather search history or type `exit` to quit the application.

---

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. **Fork the repository**
2. **Create a new branch:**
    ```bash
    git checkout -b feature/YourFeature
    ```
3. **Make your changes**
4. **Commit your changes:**
    ```bash
    git commit -m 'Add some feature'
    ```
5. **Push to the branch:**
    ```bash
    git push origin feature/YourFeature
    ```
6. **Open a pull request**

---


## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## Acknowledgements

We would like to thank the contributors and the open-source community for their valuable resources. Special thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.

