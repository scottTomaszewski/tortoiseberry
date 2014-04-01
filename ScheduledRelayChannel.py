import FakeRelayChannel
#import RelayChannel
from apscheduler.scheduler import Scheduler

class ScheduledRelayChannel:
  def __init__(self, relayChannel, schedule):
    self.channel = relayChannel
    self.schedule = schedule
    self.enabled = True
    self.sched = Scheduler()
    self.sched.daemonic = False
    self.sched.start()
    for task in schedule.tasks():
      fun = self.on if task.action == 'on' else self.off
      self.sched.add_cron_job(fun, day=task.day, hour=task.hour, minute=task.minute)
    
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
