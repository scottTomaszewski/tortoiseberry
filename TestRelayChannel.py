import RelayChannel
import time

if __name__ == "__main__":
  toTest = RelayChannel.RelayChannel(11)
  toTest.off()
  time.sleep(2)
  toTest.on()
