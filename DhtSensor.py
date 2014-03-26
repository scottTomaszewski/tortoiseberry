import subprocess

class DhtSensor:
  def name(self):
    return self.name
  
  def humidity(self):
    out = self.dht()
    if "Hum" in out:
      return out[out.index("Hum"):].split()[2]
    return -1

  def temperature(self):
    out = self.dht()
    if "Temp" in out:
      return out[out.index("Temp"):].split()[2]
    return -1

  def dht(self):
    p = subprocess.Popen(["sudo", "./Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", "2302", self.pin], stdout=subprocess.PIPE)
    return p.communicate()[0]

  def __init__(self, pin):
    if not str(pin).isdigit():
      raise Exception("invalid argument: pin expected to be positive int")
    self.pin = pin
