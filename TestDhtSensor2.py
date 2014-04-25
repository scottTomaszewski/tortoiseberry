import DhtSensor2

if __name__ == "__main__":
  toTest = DhtSensor2.DhtSensor2(4)
  print "Humidity: " + str(toTest.humidity()) + "%"
  print "Temperature: " + str(toTest.temperature()) + "c"
