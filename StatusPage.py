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
    relayChannel = RelayChannel.RelayChannel()
    sched = Schedule.Schedule()
    now = datetime.datetime.now()
    sched.add('on', '*', '*', str(now.minute+1))
    sched.add('off', '*', '*', str(now.minute+2))
    return ScheduledRelayChannel.ScheduledRelayChannel(relayChannel, sched)

  def content(self):
    status = self.overhead.status()
    content = ""
    content += "<html><head><title>Spike!</title></head>"
    content += "<body><p>Spike Status:</p>"
    content += "<p>curr: "
    content += status
    content += "<p>"
    content += "</body></html>"
    return content
