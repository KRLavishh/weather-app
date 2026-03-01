import requests

API_KEY = "4ca2cb48667bab00ac84957e9d2f9bf8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")

response = requests.get(BASE_URL, params ={
    "q": city, 
    "appid": API_KEY,
    "units": "imperial"


})

print(response.json())
