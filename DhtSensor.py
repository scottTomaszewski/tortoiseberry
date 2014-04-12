import subprocess
import threading

# The DHT sensor only updates every 2 seocnds which is the reasoning for the caching of read values
class DhtSensor:
  def humidity(self):
    out = self.lastRead
    if "Hum" in out:
      return int(float(out[out.index("Hum"):].split()[2]))
    return -1

  def temperature(self):
    out = self.lastRead
    if "Temp" in out:
      return float(out[out.index("Temp"):].split()[2])
    return -1

  def temperatureF(self):
    return int(float(9.0/5.0 * self.temperature() + 32))

  def dhtTimeout(self, count):
    p = subprocess.Popen(["sudo", "./Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", str(self.model), str(self.pin)], stdout=subprocess.PIPE)
    maybe = p.communicate()[0]
    print self.lastRead
    if 'Temp' not in maybe:
      self.dhtTimeout(count-1)
    else:
      self.lastRead = maybe

  def update(self): 
    threading.Timer(10, self.update).start(); 
    return self.dhtTimeout(3)

  def __init__(self, pin, model):
    if not str(pin).isdigit():
      raise Exception("invalid argument: pin expected to be positive int")
    self.pin = pin
    self.model = model
    self.lastRead = None
    self.update()
