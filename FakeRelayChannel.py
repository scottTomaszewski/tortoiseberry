class FakeRelayChannel:
  def __init__(self):
    self.last = None

  def on(self):
    self.last = "on"
    print "on"

  def off(self):
    self.last = "off"
    print "off"

  def status(self):
    print self.last
    return self.last
