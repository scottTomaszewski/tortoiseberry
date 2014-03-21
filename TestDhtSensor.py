import DhtSensor
import Range

if __name__ == "__main__":
  minMax = Range.Range(0,100)
  toTest = DhtSensor.DhtSensor("test", minMax, minMax, minMax, minMax)
  print "Humidity: " + str(toTest.humidity()) + "%"
  print "Temperature: " + str(toTest.temperature()) + "c"
