class FakeRelayChannel:
  def __init__(self):
    self.last = None

  def on(self):
    self.last = "on"
    print "turning on"

  def off(self):
    self.last = "off"
    print "turning off"

  def status(self):
    print "status: "
    print self.last
    return self.last
