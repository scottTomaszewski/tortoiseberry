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

  def status(self):
    return self.channel.status()

  def nextScheduledTimeAndAction(self):
    return None

