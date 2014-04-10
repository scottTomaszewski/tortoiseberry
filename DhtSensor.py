import subprocess
import time

# The DHT sensor only updates every 2 seocnds which is the reasoning for the caching of read values
class DhtSensor:
  def humidity(self):
    out = self.dht()
    if "Hum" in out:
      return int(float(out[out.index("Hum"):].split()[2]))
    return -1

  def temperature(self):
    out = self.dht()
    if "Temp" in out:
      return float(out[out.index("Temp"):].split()[2])
    return -1

  def temperatureF(self):
    return int(float(9.0/5.0 * self.temperature() + 32))

  def dht(self):
    return self.dhtTimeout(3)

  def dhtTimeout(self, count):
    # refresh only if 2 seconds has expired
    if (self.lastReadTime == None or time.time() - self.lastReadTime > 5 or 'Temp' not in self.lastRead):
      p = subprocess.Popen(["sudo", "./Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", str(self.model), str(self.pin)], stdout=subprocess.PIPE)
      self.lastRead = p.communicate()[0]
      self.lastReadTime = time.time()
      print self.lastRead
    if 'Temp' not in self.lastRead:
      return self.dhtTimeout(count-1)
    return self.lastRead

  def __init__(self, pin, model):
    if not str(pin).isdigit():
      raise Exception("invalid argument: pin expected to be positive int")
    self.pin = pin
    self.model = model
    self.lastRead = None
    self.lastReadTime = None
    self.dht()
