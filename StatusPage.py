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

  def rangeHtml(self, title, min, max, value):
    html = """
      <div class='rangeContainer'>
        <div class='rangeTitle'>T</div>
        <div class='rangeBar blueRedRange'>
    """
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
    html += """
      </div>
    </div> 
    """
    return html

  def content(self):
    vars = {}
    vars['status'] = self.overhead.status()
    vars['fooRange'] = self.rangeHtml('T', 50, 100, 73)
    content = ""
    html = open('StatusPage.html','rb')
    for line in html:
      content += Template(line).substitute(vars)
    return content
