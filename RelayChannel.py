import RPi.GPIO as GPIO
class RelayChannel:
  def on(self):
    GPIO.output(self.pin, GPIO.HIGH)

  def off(self):
    GPIO.output(self.pin, GPIO.LOW)

  def status(self):
    return 0

  def setup(self):
    if str(self.pin).isdigit():
      GPIO.setmode(GPIO.BOARD)
      GPIO.setwarnings(False) 
      GPIO.setup(self.pin, GPIO.OUT)
    else:
      raise Exception('Invalid pin: ' + str(self.pin))

  def __init__(self, gpioPin):
    self.pin = gpioPin
    self.setup()
