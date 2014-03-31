import RelayChannel
import collections

class RelayModule:
  def channelIndex(self, index):
    return self.channels.values()[index]

  def channel(self, name):
    return self.channels[name]

  def allOn(self):
    for channel in self.channels.values():
      channel.on()

  def allOff(self):
    for channel in self.channels.values():
      channel.off()

  def all(self):
    return self.channels.values()

  def __init__(self, nameToPin):
    self.channels = collections.OrderedDict()
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
