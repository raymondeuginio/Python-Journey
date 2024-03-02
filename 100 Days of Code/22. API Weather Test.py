import requests

FORECASTAPI = "https://api.openweathermap.org/data/2.5/forecast"
LAT = -6.147776
LON = 106.916641
api_key = "41a3f05b2f2a1bfed6ddd9d2f4880a32"

weather_params = {
    "lat": -6.147776,
    "lon": 106.916641,
    "appid": api_key,
    "lang" : "id",
    "cnt": 6,
    "units": "metric"
}
# https://api.openweathermap.org/data/2.5/weather?lat=-6.147776&lon=106.916641&appid=41a3f05b2f2a1bfed6ddd9d2f4880a32

respons = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=weather_params)
respons.raise_for_status()
weather_data = respons.json()["list"]

for i in weather_data:
    if int(i["weather"][0]["id"]) < 800:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")
