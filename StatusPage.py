import RelayChannel
import ScheduledRelayChannel
import Schedule
from string import Template
import math

#temp
import datetime

class StatusPage:
  def __init__(self):
    self.overhead = self.spikeOverheadLight()
    self.overhead.off()

  def spikeOverheadLight(self):
    relayChannel = RelayChannel.RelayChannel(11)
    sched = Schedule.Schedule()
    now = datetime.datetime.now()
    sched.add('on', '*', '*', str(now.minute+1))
    sched.add('off', '*', '*', str(now.minute+2))
    return ScheduledRelayChannel.ScheduledRelayChannel(relayChannel, sched)

  def parse(self, form):
    if 'overheadOn' in form:
      self.overhead.on()
    if 'overheadOff' in form:
      self.overhead.off()

  def rangeHtml(self, title, min, max, value, cssBackground):
    html = "<div class='rangeTitle'>" + str(title) + "</div>"
    html += "<div class='rangeBar " + cssBackground + "'>"
    perc = float(value-min) / (max-min)
    mark = math.floor(perc * 41)
    for i in range(1, 41):
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
    vars['topLeftTemp'] = self.temperatureRangeHtml(73)
    vars['topLeftHumidity'] = self.humidityRangeHtml(68)
    content = ""
    html = open('StatusPage.html','rb')
    for line in html:
      content += Template(line).substitute(vars)
    return content
