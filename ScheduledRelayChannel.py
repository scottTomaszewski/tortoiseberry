import RelayChannel

class ScheduledRelayChannel:
  def __init__(self, relayChannel, schedule):
    self.channel = relayChannel
    self.schedule = schedule
    self.enabled = True

  def on(self):
    return self.channel.on()

  def off(self):
    return self.channel.off()

  def status(self):
    return self.channel.status()

  def enabled(boolean)
    self.enabled = boolean

  def nextScheduledTimeAndAction(self):
    return None
      
