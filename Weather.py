import json
import urllib
import time


class Weather:
    def __init__(self):
        self.last_checked = None
        self.weather = None

    def temperature(self):
        return self.k2f(self.data()['main']['temp'])

    def temp_high(self):
        return self.k2f(self.data()['main']['temp_max'])

    def temp_low(self):
        return self.k2f(self.data()['main']['temp_min'])

    def icon_url(self):
        icon = self.data()['weather'][0]['icon']
        return "http://openweathermap.org/img/w/" + icon + ".png"

    def icon(self):
        id = self.data()['weather'][0]['id']
        return '/images/' + str(self.codeToIcon(id))

    def data(self):
        five_minutes = 300
        if self.last_checked == None or time.time() - self.last_checked > five_minutes:
            json_weather = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?id=4049032").read()
            self.weather = json.loads(json_weather)
            self.last_checked = time.time()
        return self.weather

    def k2c(self, t):
        return t - 273.15

    def k2f(self, t):
        return (t * 9 / 5.0) - 459.67

    def codeToIcon(self, code_string):
        code = int(code_string)
        if code >= 200 and code < 300:
            return 'storm.png'
        if code >= 300 and code < 400:
            return 'chance of rain.png'
        if code == 511:
            return 'rain snow.png'
        if code >= 500 and code < 600:
            return 'rain.png'
        if code == 600:
            return 'light snow.png'
        if code >= 601 and code < 612:
            return 'snow.png'
        if code >= 612 and code < 700:
            return 'icy.png'
        if code >= 701 and code < 722:
            return 'mist.png'
        if code >= 731 and code < 800:
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
