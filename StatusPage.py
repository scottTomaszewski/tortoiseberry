import RelayChannel
import ScheduledRelayChannel
import Schedule
import DhtSensor
from string import Template
import math
import Weather

#temp
import datetime

class StatusPage:
  def __init__(self):
    self.overhead = self.spikeOverheadLight()
    self.overhead.off()
    self.basking = self.spikeBaskingLight()
    self.basking.off()
    self.topLeftDHT = DhtSensor.DhtSensor(4, 22)
    self.topRightDHT = DhtSensor.DhtSensor(14, 11)
    self.bottomLeftDHT = DhtSensor.DhtSensor(15, 11)
    self.bottomRightDHT = DhtSensor.DhtSensor(18, 11)
    self.weather = Weather.Weather()

  def spikeOverheadLight(self):
    relayChannel = RelayChannel.RelayChannel(11)
    sched = Schedule.Schedule()
    now = datetime.datetime.now()
    sched.add('on', '*', '10', '0')
    sched.add('off', '*', '22', '0')
    #sched.add('on', '*', '*', str(now.minute+2))
    #sched.add('off', '*', '*', str(now.minute+3))
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

  def rangeHtml(self, title, min, max, value, cssBackground):
    html = "<div class='rangeTitle'>" + str(title) + "</div>"
    html += "<div class='rangeBar " + cssBackground + "'>"
    perc = float(value-min) / (max-min)
    mark = math.floor(perc * 45) if perc > 0 else 1
    for i in range(1, 45):
      if i == mark-1 or i == mark+1:
        html += "<div class='rangeTick rangeTickMed'></div>"
      elif i == mark:
        html += "<div class='rangeTick rangeTickLarge'>"
        html += "  <div class='rangeTickValue'>" + str(value) + "</div>"
        html += "</div>"
      else:
        html += "<div class='rangeTick'></div>"
    html += "</div>"
    return html

  def temperatureRangeHtml(self, value):
    return self.rangeHtml('T', 50, 100, value, 'blueRedFullRange')

  def humidityRangeHtml(self, value):
    return self.rangeHtml('H', 30, 90, value, 'redBlueFullRange')

  def content(self):
    vars = {}
    vars['uvbStatus'] = 'OFF' if self.overhead.status() == 1 else 'ON'
    vars['baskingStatus'] = 'OFF' if self.basking.status() == 1 else 'ON'
    
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
