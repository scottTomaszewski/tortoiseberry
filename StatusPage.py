import RelayChannel
import ScheduledRelayChannel
import Schedule
from string import Template

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

  def content(self):
    vars = {}
    vars['status'] = self.overhead.status()
    content = ""
    html = open('htmlDesign.html','rb')
    for line in html:
      content += Template(line).substitute(vars)
      

#    content += "<html><head><title>Spike!</title></head>"
#    content += "<body><p>Spike Status:</p>"
#    content += "<p>curr: "
#    content += str(status)
#    content += "<p>"
#    content += """
#    <form action="MyRequestHandler.py" method="post">
#      Overhead Light: 
#      <input type="submit" value="On" name='overheadOn' />
#      <input type="submit" value="Off" name='overheadOff' />
#    </form>
#    """
#    content += "</body></html>"
    return content
