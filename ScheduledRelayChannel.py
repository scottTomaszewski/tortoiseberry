import RelayChannel

class ScheduledRelayChannel:
  def on(self):
    self.reasonForLastChange = "Manually set from " + str(self.status()) + " to OFF"
    return self.channel.on()

  def on(self, reason):
    self.on()
    self.reasonForLastChange += "because: " + str(reason)

  def off(self):
    self.reasonForLastChange = "Manually set from " + str(self.status()) + " to OFF"
    return self.channel.off()

  def off(self, reason):
    self.off()
    self.reasonForLastChange += "because: " + str(reason)
 
 def status(self):
    return self.channel.status()

  def nextTimeAndAction(self):
    return None

  def reasonForLastChange(self):
    return self.reasonForLastChange

  def __init__(self, relayChannel, schedule):
    self.channel = relayChannel
    self.schedule = schedule
    self.reasonForLastChange = "Never changed"
