import FakeRelayChannel
#import RelayChannel
from apscheduler.scheduler import Scheduler
import atexit

class ScheduledRelayChannel:
  def __init__(self, relayChannel, schedule):
    self.channel = relayChannel
    self.schedule = schedule
    self.enabled = True
    self.sched = Scheduler()
    self.sched.daemonic = False
    self.sched.start()
    atexit.register(lambda: self.sched.shutdown(wait=False))
    for task in schedule.tasks():
      fun = self.on if task.action == 'on' else self.off
      self.sched.add_cron_job(fun, day=task.day, hour=task.hour, minute=task.minute)
    
 #   test_log = open('daemon.log', 'w')
 #   daemon.DaemonContext.files_preserve = [test_log]

 #   try:
 #     with daemon.DaemonContext():
 #       from datetime import datetime
 #       from apscheduler.scheduler import Scheduler
 #       import signal
 #
 #       logging.basicConfig(level=logging.DEBUG)
 #       sched = init_schedule()
 #
 #       print schedule.tasks()
 #       for task in schedule.tasks():
 #         fun = self.on if task.action == 'on' else self.off
 #         self.sched.add_cron_job(fun, day=task.day, hour=task.hour, minute=task.minute)
 #       signal.pause()
 #   except Exception, e:
 #     print e
 
 # def init_schedule():
 #   sched = Scheduler()
 #   sched.standalone = True
 #   sched.start()
 #   return sched

  def on(self):
    return self.channel.on()

  def off(self):
    return self.channel.off()

  def status(self):
    return self.channel.status()

  def enabled(boolean):
    self.enabled = boolean
     
  def shutdown(self):
    self.sched.shutdown(wait=False)
