import RelayChannel

class ScheduledRelayChannel:
  def __init__(self, relayChannel, schedule):
    self.channel = relayChannel
    self.schedule = schedule
    self.reasonForLastChange = "Never changed"

  def on(self):
    self.manuallyChangedReason(self.status(), "ON")
    return self.channel.on()

  def off(self):
    self.manuallyChangedReason(self.status(), "OFF")
    return self.channel.off()

  def manuallyChangedReason(self, from, to):
    self.reasonForLastChange = "Manually set from " + str(from) + " to " + str(to)

  def status(self):
    return self.channel.status()

  def nextScheduledTimeAndAction(self):
    return None

  def reasonForLastChange(self):
    return self.reasonForLastChange

