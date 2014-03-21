import subprocess

Class dht11_sensor:
  def name(self):
    return self.name
  
  def expected_temperature(self):
    return self.expected_temp

  def absolute_temperature(self):
    return self.absolute_temp

  def expected_humidity(self):
    return self.expected_humidity

  def absolute_humidity(self):
    return self.absolute_humidity

  def humidity(self):
    if "Hum" in self.dht():
      return out[out.index("Hum"):].split()[2]
    return -1

  def temperature(self):
    if "Temp" in self.dht():
      return out[out.index("Temp"):].split()[2]
    return -1

  def dht(self):
    p = subprocess.Popen(["sudo", "./Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", "2302", "4"], stdout=subprocess.PIPE)
    return p.communicate()[0]

  def is_within_expected_humidity(self):
    return self.compare_to_expected_humidity() == 0

  def compare_to_expected_humidity(self):
    return self.expected_humidity.compare_to(self.humidity())

  def is_within_absolute_humidity(self):
    return self.compare_to_absolute_humidity() == 0

  def compare_to_absolute_humidity(self):
    return self.absolute_humidity.compare_to(self.humidity())

  def is_within_expected_temp(self):
    return self.compare_to_absolute_temp() == 0

  def compare_to_expected_temp(self):
    return self.expected_temps.compare_to(self.temperature())

  def is_within_absolute_temp(self):
    return self.compare_to_absolute_temp() == 0

  def compare_to_absolute_temp(self):
    return self.absolute_temps.compare_to(self.temperature())
    
  def __intt__(name, expected_temperatures, absolute_temperatures, expected_humidity, absolute_humidity):
    self.name = name
    self.expected_temps = expected_temperatures
    self.absolute_temps = absolute_temperatures
    self.expected_humidity = expected_humidity
    self.absolute_humidity = absolute_humidity
