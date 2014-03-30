import DhtSensor

class HumidityTemperatureSensor:
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
    return self.sensor.humidity()

  def temperature(self):
    return self.sensor.temperature()

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
    
  def __init__(self, name, pin, expected_temperatures, absolute_temperatures, expected_humidity, absolute_humidity):
    self.name = name
    self.expected_temps = expected_temperatures
    self.absolute_temps = absolute_temperatures
    self.expected_humidity = expected_humidity
    self.absolute_humidity = absolute_humidity
    self.sensor = DhtSensor.DhtSensor(pin)
  
  @classmethod
  def withRanges(cls, name, pin, expected_temperatures, absolute_temperatures, expected_humidity, absolute_humidity):
    return cls(name, pin, expected_temperatures, absolute_temperatures, expected_humidity, absolute_humidity)

  @classmethod
  def withoutRanges(cls, name, pin):
    fullRange = Range.Range(0, 100)
    return cls(name, pin, fullRange, fullRange, fullRange, fullRange)
