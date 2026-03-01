import requests

API_KEY = "4ca2cb48667bab00ac84957e9d2f9bf8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("\nEnter a city (or q to quit): ")

    if city == "":
        print("Please enter a city.")
        continue

    if city.lower() == "q":
        print("Come again sometime!")
        break
    
    try:
        response = requests.get(BASE_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "imperial"
        })
    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your connection and try again.")
        continue

    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°F")
        print(f"Feels like: {data['main']['feels_like']}°F")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description']}")
    else:
        print("City not found, try again.")




       


    
