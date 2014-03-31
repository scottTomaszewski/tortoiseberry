import RelayChannel

class NotifyingRelayChannel:
  def __init__(self, relayChannel, listener):
    self.channel = relayChannel
    self.listener = listener

  def on(self):
    self.channel.on()
    self.listener.notify()

  def off(self):
    self.channel.off()
    self.listener.notify()

  def status(self):
    return self.channel.status()
