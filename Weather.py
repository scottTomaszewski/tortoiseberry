import json
import urllib
import time


class Weather:
    def __init__(self):
        self.last_checked = None
        self.weather = None

    def temperature(self):
        return k2f(self.data()['main']['temp'])

    def temp_high(self):
        return k2f(self.data()['main']['temp_max'])

    def temp_low(self):
        return k2f(self.data()['main']['temp_min'])

    def icon_url(self):
        icon = self.data()['weather'][0]['icon']
        return "http://openweathermap.org/img/w/" + icon + ".png"

    def icon(self):
        id = self.data()['weather'][0]['id']
        return '/images/' + str(code_to_icon(id))

    def data(self):
        five_minutes = 300
        if self.last_checked == None or time.time() - self.last_checked > five_minutes:
            json_weather = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?id=4049032").read()
            self.weather = json.loads(json_weather)
            self.last_checked = time.time()
        return self.weather


def code_to_icon(code_string):
    code = int(code_string)
    if 200 <= code < 300:
        return 'storm.png'
    if 300 <= code < 400:
        return 'chance of rain.png'
    if code == 511:
        return 'rain snow.png'
    if 500 <= code < 600:
        return 'rain.png'
    if code == 600:
        return 'light snow.png'
    if 601 <= code < 612:
        return 'snow.png'
    if 612 <= code < 700:
        return 'icy.png'
    if 701 <= code < 722:
        return 'mist.png'
    if 731 <= code < 800:
        return 'fog.png'
    if code == 800:
        return 'sunny.png'
    if code == 801:
        return 'mostly sunny.png'
    if code == 802:
        return 'partly sunny.png'
    if code == 803:
        return 'partly cloudy.png'
    if code == 804:
        return 'mostly cloudy.png'
    return 'unknown.png'


def k2f(t):
    return (t * 9 / 5.0) - 459.67


def k2c(t):
    return t - 273.15

