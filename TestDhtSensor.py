import DhtSensor

if __name__ == "__main__":
  toTest = DhtSensor.DhtSensor(4, '11')
  print "Humidity: " + str(toTest.humidity()) + "%"
  print "Temperature: " + str(toTest.temperature()) + "c"
