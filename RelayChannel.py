import RPi.GPIO as GPIO

class RelayChannel:
  def on(self):
    GPIO.output(self.pin, GPIO.LOW)

  def off(self):
    GPIO.output(self.pin, GPIO.HIGH)

  def status(self):
    return GPIO.input(self.pin)

  def __init__(self, gpioPin):
    if str(gpioPin).isdigit():
      self.pin = gpioPin
      GPIO.setmode(GPIO.BOARD)
      GPIO.setwarnings(False) 
      GPIO.setup(self.pin, GPIO.OUT)
    else:
      raise Exception('Invalid pin: ' + str(gpioPin))
