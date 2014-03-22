import RelayChannel
import time

if __name__ == "__main__":
  toTest = RelayChannel.RelayChannel(11)
  toTest.off()
  print "status: " + str(toTest.status())
  time.sleep(2)
  toTest.on()
  print "status: " + str(toTest.status())
