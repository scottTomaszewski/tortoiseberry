import RelayChannel

class RelayModule:
  def channel(self, index):
    return self.channels[index]

  def __init__(self, pinList):
    self.channels = {}
    for idx, pin in enumerate(pinList):
      self.channels[idx] = RelayChannel.RelayChannel(pin)
