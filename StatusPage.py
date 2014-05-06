import RelayChannel
from apscheduler.schedule import Scheduler
import DHT11
from string import Template
import math
import Weather

class StatusPage:
  def __init__(self):
    scheduler = Scheduler()
    self.overhead = self.spikeOverheadLight(scheduler)
    self.basking = self.spikeBaskingLight(scheduler)
    self.topLeftDHT = DHT11.DHT11_sensor(4)
    self.topRightDHT = DHT11.DHT11_sensor(14)
    self.bottomLeftDHT = DHT11.DHT11_sensor(15)
    self.bottomRightDHT = DHT11.DHT11_sensor(18)
    self.topLeftDHT.autoUpdate()
    self.topRightDHT.autoUpdate()
    self.bottomLeftDHT.autoUpdate()
    self.bottomRightDHT.autoUpdate()
    self.weather = Weather.Weather()

  def spikeOverheadLight(self, sched):
    relayChannel = RelayChannel.RelayChannel(11, sched)
    relayChannel.turnOnDailyAt('10', '0')
    relayChannel.turnOffDailyAt('22', '0')
    relayChannel.off()
    return relayChannel

  def spikeBaskingLight(self, sched):
    relayChannel = RelayChannel.RelayChannel(13, sched)
    relayChannel.turnOnDailyAt('12', '0')
    relayChannel.turnOffDailyAt('15', '0')
    relayChannel.off()
    return relayChannel

  def parse(self, form):
    if 'overheadOn' in form:
      self.overhead.on()
    if 'overheadOff' in form:
      self.overhead.off()
    if 'baskingOn' in form:
      self.basking.on()
    if 'baskingOff' in form:
      self.basking.off()

  def data(self):
    vars = {}
    vars['uvbStatus'] = 'OFF' if self.overhead.status() == 1 else 'ON'
    vars['baskingStatus'] = 'OFF' if self.basking.status() == 1 else 'ON'
    
    vars['topLeftTempValue'] = self.topLeftDHT.temperatureF()
    vars['topRightTempValue'] = self.topRightDHT.temperatureF()
    vars['bottomLeftTempValue'] = self.bottomLeftDHT.temperatureF()
    vars['bottomRightTempValue'] = self.bottomRightDHT.temperatureF()

    vars['topLeftHumidityValue'] = self.topLeftDHT.humidity()
    vars['topRightHumidityValue'] = self.topRightDHT.humidity()
    vars['bottomLeftHumidityValue'] = self.bottomLeftDHT.humidity()
    vars['bottomRightHumidityValue'] = self.bottomRightDHT.humidity()
    
    vars['weatherIcon'] = self.weather.icon()
    vars['outsideTemp'] = int(self.weather.temperature())
    vars['outsideMinTemp'] = int(self.weather.tempLow())
    vars['outsideMaxTemp'] = int(self.weather.tempHigh())
    return vars

  def content(self):
    content = ""
    html = open('StatusPage.html','rb')
    for line in html:
      content += Template(line).substitute(self.data())
    return content

  def update(self):
    return json.dumps(self.data())
