import RelayChannel
import ScheduledRelayChannel
import Schedule
import time
import sys
import os
import datetime

def fake():
  channel = RelayChannel.RelayChannel(11)
  channel.on()
  channel.off()
  channel.status()

  sched = Schedule.Schedule()
  now = datetime.datetime.now()
  sched.add('on', '*', '*', str(now.minute+1))
  scheduled = ScheduledRelayChannel.ScheduledRelayChannel(channel, sched)
  try:
    time.sleep(60)
    scheduled.shutdown()
  except KeyboardInterrupt:
    print 'Interrupted'
    scheduled.shutdown()
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)

def real():
  toTest = RelayChannel.RelayChannel(11)
  toTest.off()
  print "status: " + str(toTest.status())
  time.sleep(2)
  toTest.on()
  print "status: " + str(toTest.status())

if __name__ == "__main__":
  fake()

