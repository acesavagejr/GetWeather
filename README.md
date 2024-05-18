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

## Building WeatherPlug
First,Download the source code (python scripts) and open your terminal.

Second, type ``` pip install setuptools wheel twine ```

Then type ``` python setup.py sdist bdist_wheel ```.

After that type ``` pip install dist/GetWeather-[Version]-py3-none-any.whl ``` Make sure to replace "version" with the version number of the source code

The once its installed you have now builed WeatherPlug!
