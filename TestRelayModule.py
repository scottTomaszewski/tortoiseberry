import RelayModule
import time

wait = 1

def unnamed():
  print "===Unnamed Test==="
  toTest = RelayModule.RelayModule.unnamed([11])
  print "by channel"
  toTest.channel(0).on()
  print toTest.channel(0).status()
  time.sleep(wait)
  toTest.channel(0).off()
  print toTest.channel(0).status()
  
  time.sleep(wait)
  
  print "by index"
  toTest.channelIndex(0).on()
  print toTest.channelIndex(0).status()
  time.sleep(wait)
  toTest.channelIndex(0).off()
  print toTest.channelIndex(0).status()
  

def named():
  print "===Named Test==="
  
if __name__ == "__main__":
  unnamed()
  named()
