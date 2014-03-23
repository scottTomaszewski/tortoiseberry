import RelayModule
import time

if __name__ == "__main__":
  toTest = RelayModule.RelayModule.unnamed([11])
  toTest.channel(0).on()
  toTest.channel(0).status()
  time.sleep(2)
  toTest.channel(0).off()
  toTest.channel(0).status()
