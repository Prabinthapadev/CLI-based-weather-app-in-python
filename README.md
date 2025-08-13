# 🌦 CLI Weather App

A simple **Command-Line Interface (CLI)** application that fetches and displays the current weather conditions for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## 📌 Features
- Get **real-time weather data** for any city.
- Shows:
  - City name
  - Temperature (°C)
  - Weather description
  - Humidity percentage
- Handles invalid city names gracefully.
- Simple and beginner-friendly Python code.

---

## 📂 Project Structure

weatherapp.py
README.md


---

## 🛠 Requirements
- Python 3.x
- `requests` library

Install `requests` using:
```bash
pip install requests

🔑 API Key Setup

This app uses the OpenWeatherMap API.

    Go to OpenWeatherMap and create a free account.

    Generate your API key from your account dashboard.

    Replace API_KEY in weatherapp.py with your API key:

    API_KEY = "YOUR_API_KEY_HERE"

▶️ Usage

Run the program in your terminal:

python weatherapp.py

Example:

*********************************
A simple CLI based weather app to check current weather condition
Enter city name to check weather: London
City: London
Temperature: 18°C
Weather: broken clouds
Humidity: 65%

⚠️ Error Handling

    If the city name is incorrect or not found, the app will show:

    Error: city not found

    The app will not crash on invalid input.

📜 License

This project is licensed under the MIT License - you are free to use and modify it.
