import FakeRelayChannel
from apscheduler.scheduler import Scheduler

class ScheduledRelayChannel:
  def __init__(self, relayChannel, schedule):
    self.channel = relayChannel
    self.schedule = schedule
    self.enabled = True
    self.sched = Scheduler()
    self.sched.start()
    for task in schedule.tasks():
      fun = self.scheduledOn if task.action == 'on' else self.scheduledOff
      self.sched.add_cron_job(fun, day=task.day, hour=task.hour, minute=task.minute)
    
  def on(self):
    return self.channel.on()

  def off(self):
    return self.channel.off()

  def status(self):
    return self.channel.status()

  def enabled(boolean):
    self.enabled = boolean

  def isEnabled(self):
    return self.enabled
  
  def scheduledOn(self):
    print "Schedule invoked: on"
    if self.enabled:
      return self.on()
    return 'Scheduled On not run because disabled'

  def scheduledOff(self):
    print "Schedule invoked: off"
    if self.enabled:
      return self.off()
    return 'Scheduled Off not run because disabled'

  def shutdown(self):
    self.sched.shutdown(wait=False)
