import RelayChannel

class RelayModule:
  def channelIndex(self, index):
    return self.channels.values[index]

  def channel(self, name):
    return self.channels[name]

  #def allOn():

  def __init__(self, nameToPin):
    self.channels = {}
    for name, pin in nameToPin.iteritems():
      self.channels[name] = RelayChannel.RelayChannel(pin)

  @classmethod
  def unnamed(cls, pinList):
    indexToPin = {}
    for idx, pin in enumerate(pinList):
      indexToPin[idx] = pin
    return cls(indexToPin)

  @classmethod
  def named(cls, nameToPin):
    return cls(nameToPin)
