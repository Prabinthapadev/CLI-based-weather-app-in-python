import requests

# API details
API_KEY = "a1a8c5dce307d24ffce94baac1f840c7"

print("*********************************")
print("A simple CLI based weather app to check current weather condition")

city = input("Enter city name to check weather: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Accessing the response from the API
response = requests.get(url)
data = response.json()

# Error handling
if response.status_code != 200 or data.get("cod") != 200:
    print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
else:
    # Printing weather data
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
