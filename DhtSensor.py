import subprocess
import time

# The DHT sensor only updates every 2 seocnds which is the reasoning for the caching of read values
class DhtSensor:
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
    # refresh only if 2 seconds has expired
    if (time.time() - self.lastReadTime > 2):
      p = subprocess.Popen(["sudo", "./Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", "2302", str(self.pin)], stdout=subprocess.PIPE)
      self.lastRead = p.communicate()[0]
      self.lastReadTime = time.time()
    return self.lastRead

  def __init__(self, pin):
    if not str(pin).isdigit():
      raise Exception("invalid argument: pin expected to be positive int")
    self.pin = pin
    self.lastRead = None
    self.lastReadTime = None
    self.dht()
