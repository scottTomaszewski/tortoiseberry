import RelayChannel
import ScheduledRelayChannel
import Schedule
import DHT11
from string import Template
import math
import Weather
import pigpio

#temp 
import datetime

class StatusPage:
  def __init__(self):
    pigpio.start()
    self.overhead = self.spikeOverheadLight()
    self.overhead.off()
    self.basking = self.spikeBaskingLight()
    self.basking.off()
    self.topLeftDHT = DHT11.DHT11_sensor(4)
    self.topRightDHT = DHT11.DHT11_sensor(14)
    self.bottomLeftDHT = DHT11.DHT11_sensor(15)
    self.bottomRightDHT = DHT11.DHT11_sensor(18)
    self.topLeftDHT.autoUpdate()
    self.topRightDHT.autoUpdate()
    self.bottomLeftDHT.autoUpdate()
    self.bottomRightDHT.autoUpdate()
    self.weather = Weather.Weather()

  def spikeOverheadLight(self):
    relayChannel = RelayChannel.RelayChannel(11)
    sched = Schedule.Schedule()
    now = datetime.datetime.now()
    sched.add('on', '*', '10', '0')
    sched.add('off', '*', '22', '0')
    return ScheduledRelayChannel.ScheduledRelayChannel(relayChannel, sched)

  def spikeBaskingLight(self):
    relayChannel = RelayChannel.RelayChannel(13)
    sched = Schedule.Schedule()
    now = datetime.datetime.now()
    sched.add('on', '*', '12', '0')
    sched.add('off', '*', '15', '0')
    return ScheduledRelayChannel.ScheduledRelayChannel(relayChannel, sched)

  def parse(self, form):
    if 'overheadOn' in form:
      self.overhead.on()
    if 'overheadOff' in form:
      self.overhead.off()
    if 'baskingOn' in form:
      self.basking.on()
    if 'baskingOff' in form:
      self.basking.off()

  def rangeHtml(self, title, units, min, max, value, cssBackground):
    html = "<div class='rangeTitle'>" + str(title) + "<span class='rangeTitleUnits'>" + str(units) + "</span></div>"
    html += "<div class='rangeBar " + cssBackground + "'>"
    perc = float(value-min) / (max-min)
    mark = math.floor(perc * 45) if perc > 0 else 1
    for i in range(1, 45):
      if i == mark-1 or i == mark+1:
        html += "<div class='rangeTick rangeTickMed'></div>"
      elif i == mark:
        html += "<div class='rangeTick rangeTickLarge'>"
        html += "</div>"
      else:
        html += "<div class='rangeTick'></div>"
    html += "</div>"
    return html

  def temperatureRangeHtml(self, value):
    return self.rangeHtml(str(value), 'F', 50, 100, value, 'blueRedFullRange')

  def humidityRangeHtml(self, value):
    return self.rangeHtml(str(value), '%', 30, 90, value, 'redBlueFullRange')

  def printData(self):
    print "top left temp: " + str(self.topLeftDHT.temperatureF())
    print "top right temp: " + str(self.topRightDHT.temperatureF())
    print "bottom left temp: " + str(self.bottomLeftDHT.temperatureF())
    print "bottom right temp: " + str(self.bottomRightDHT.temperatureF())

    print "top left hum: " + str(self.topLeftDHT.humidity())
    print "top right hum: " + str(self.topRightDHT.humidity())
    print "bottom left hum: " + str(self.bottomLeftDHT.humidity())
    print "bottom right hum: " + str(self.bottomRightDHT.humidity())

  def content(self):
    vars = {}
    vars['uvbStatus'] = 'OFF' if self.overhead.status() == 1 else 'ON'
    vars['baskingStatus'] = 'OFF' if self.basking.status() == 1 else 'ON'
   
    # trigger dht sensors
#    self.topLeftDHT.trigger()
#    self.topRightDHT.trigger()
#    self.bottomLeftDHT.trigger()
#    self.bottomRightDHT.trigger()

    vars['topLeftTemp'] = self.temperatureRangeHtml(self.topLeftDHT.temperatureF())
    vars['topRightTemp'] = self.temperatureRangeHtml(self.topRightDHT.temperatureF())
    vars['bottomLeftTemp'] = self.temperatureRangeHtml(self.bottomLeftDHT.temperatureF())
    vars['bottomRightTemp'] = self.temperatureRangeHtml(self.bottomRightDHT.temperatureF())

    vars['topLeftHumidity'] = self.humidityRangeHtml(self.topLeftDHT.humidity())
    vars['topRightHumidity'] = self.humidityRangeHtml(self.topRightDHT.humidity())
    vars['bottomLeftHumidity'] = self.humidityRangeHtml(self.bottomLeftDHT.humidity())
    vars['bottomRightHumidity'] = self.humidityRangeHtml(self.bottomRightDHT.humidity())

    vars['weatherIcon'] = self.weather.icon()
    vars['outsideTemp'] = int(self.weather.temperature())
    vars['outsideMinTemp'] = int(self.weather.tempLow())
    vars['outsideMaxTemp'] = int(self.weather.tempHigh())

    content = ""
    html = open('StatusPage.html','rb')
    for line in html:
      content += Template(line).substitute(vars)
    return content
  
  def exit(self):
    pigpio.stop()
