def GetWeather(city):
  import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=16d123a52e5c07ef13e101ad033248ea&units=metric'.format(city)

res = requests.get(url)
data = res.json()

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']
