# WeatherPlug
a python libary to get weather data easly (powered by OpenWeather)

## Installation
To install type ``` pip install WeatherPlug ```

## Using WeatherPlug
to use WeatherPlug make a python file and start it with this
``` from WeatherPlug import WeatherPlug ```
after that type
``` city = input("Type a city!") ```
Now to request weather type
``` WeatherPlug(city) ```
and to print the results
``` print(WeatherPlug.temp) ```
``` print(WeatherPlug.humidity) ```
``` print(WeatherPlug.wind) ```
``` print(WeatherPlug.desc) ```
