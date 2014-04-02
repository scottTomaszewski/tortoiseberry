import FakeRelayChannel
import ScheduledRelayChannel
import Schedule

#temp
import datetime

class StatusPage:
  def __init__(self):
    self.scheduled = self.light()

  def light(self):
    relayChannel = FakeRelayChannel.FakeRelayChannel()
    sched = Schedule.Schedule()
    now = datetime.datetime.now()
    sched.add('on', '*', '*', str(now.minute+1))
    return ScheduledRelayChannel.ScheduledRelayChannel(relayChannel, sched)

  def content(self):
    content = ""
    content += "<html><head><title>Spike!</title></head>"
    content += "<body><p>Spike Status:</p>"
    content += "<p>"
    content += str(self.scheduled.status())
    content += "<p>"
    content += "</body></html>"
