class RelayChannel:
  def on(self):
    with open(self.dir + "value", "w") as f:
      f.write("0")

  def off(self):
    with open(self.dir + "value", "w") as f:
      f.write("1")

  def status(self):
    with open(self.dir + "value", "r") as f:
      return f.read()

  def setup(self):
    if str(self.pin).isdigit():
      # Enable pin access via the Kernel on path '/sys/class/gpio/'
      with open("/sys/class/gpio/export","a") as f:
        f.write(str(self.pin))

      # configure as output
      with open(self.dir + "direction","w") as f:
        f.write('out')
    else:
      raise Exception('Invalid pin: ' + str(self.pin))

  def __init__(self, gpioPin):
    self.pin = gpioPin
    self.dir = "/sys/class/gpio/gpio" + str(self.pin) + "/"
    self.setup()
