# weather_data_fetcher.py

import requests

# Your API key (replace with your own from OpenWeatherMap)
API_KEY = "7f9b6a9ecc75f31e3bdec60ceb5e4155"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Ask user for city name
city = input("Enter city name: ")

# Create request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Send request to API
response = requests.get(url)

# Process response
if response.status_code == 200:
    data = response.json()
    main = data["main"]
    temperature = main["temp"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    weather = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Condition: {weather}")
else:
    print("Error fetching data. Please check the city name or API key.")
