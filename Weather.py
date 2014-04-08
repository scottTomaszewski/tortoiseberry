import json, urllib
from pprint import pprint
import time

class Weather:
  def __init__(self):
    self.lastChecked = None
    self.weather = None

  def temperature(self):
    return self.k2f(self.data()['main']['temp'])

  def tempHigh(self):
    return self.k2f(self.data()['main']['temp_max'])

  def tempLow(self):
    return self.k2f(self.data()['main']['temp_min'])

  def data(self):
    fiveMinutes = 300
    if self.lastChecked == None or time.time() - self.lastChecked > fiveMinutes:
      jsonWeather = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?id=4049032").read()
      self.weather = json.loads(jsonWeather)
      self.lastChecked = time.time()
      print 'fresh'
    return self.weather

  def k2c(self, t):
    return t-273.15
  
  def k2f(self, t):
    return (t*9/5.0)-459.67
  
