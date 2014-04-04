import RelayChannel
import ScheduledRelayChannel
import Schedule

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
    overhead = form.getvalue('overheadLight')
    if overhead == 'on':
      self.overhead.on()
    elif overhead == 'off':
      self.overhead.off()
    else:
      print "" + str(overhead) + " is not a valid option for overhead lights"

  def content(self):
    status = self.overhead.status()
    content = ""
    content += "<html><head><title>Spike!</title></head>"
    content += "<body><p>Spike Status:</p>"
    content += "<p>curr: "
    content += str(status)
    content += "<p>"
    content += """
    <form action="MyRequestHandler.py" method="post">
      <input type="radio" name="overheadLight" value="on" /> On
      <input type="radio" name="overheadLight" value="off" /> Off
      <input type="submit" value="Submit" />
    </form>
    """
    content += "</body></html>"
    return content
