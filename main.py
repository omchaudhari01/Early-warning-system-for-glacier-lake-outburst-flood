import requests
import json
from Widget import Widget
import os.path

# Get IP address:
ip = requests.get('https://checkip.amazonaws.com').text

# Get latitude and longitude from IP address:
request_url = 'https://geolocation-db.com/jsonp/' + ip
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
latitude = result['latitude']
longitude = result['longitude']
city = result['city']

# Get weather data using latitude and longitude :
try:
    forecast_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m," \
               "relativehumidity_2m,precipitation,weathercode,windspeed_10m&daily=temperature_2m_max," \
               "temperature_2m_min,sunrise,sunset&timezone=auto".format(latitude, longitude)
    forecast = requests.get(forecast_url)
    forecast_data = forecast.content.decode()

    file = open("json_weather.txt", "w")
    file.write(forecast_data)
    file.close()

    forecast_data = json.loads(forecast_data)
    # print(json.dumps(forecast_data, indent=4, sort_keys=True))
    Widget(forecast_data, city, False)

except Exception as e:
    filename = "json_weather.txt"
    if os.path.isfile(filename):
        file = open("json_weather.txt", "r")
        lines = file.readlines()
        forecast_data = lines[0]
        forecast_data = json.loads(forecast_data)
        Widget(forecast_data, city, True)

''' 
# API key:
API key:         l1xeuPlkJkMUnQOTQWkUn4W3eJ8arGWG 

# Get location key using latitude and longitude:
location_url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=l1xeuPlkJkMUnQOTQWkUn4W3eJ8arGWG&q={}%2C{}".format(latitude, longitude)
location = requests.get(location_url)
location_data = location.json()
print(location_data)
print(latitude, longitude)
location_key = location_data['Key']

# Get current weather data using location key:
forecast_url = "http://dataservice.accuweather.com/currentconditions/v1/{}?apikey=l1xeuPlkJkMUnQOTQWkUn4W3eJ8arGWG".format(location_key, latitude, longitude)
forecast = requests.get(forecast_url)
forecast_data = forecast.json()

# Print weather data:
print(forecast_data) '''