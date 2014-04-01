class Schedule:
  def __init__(self, action, day, hour, minute):
    self.action = action
    self.day = day
    self.hour = hour
    self.minute = minute

  def action(self):
    return self.action

  def day(self):
    return self.day

  def hour(self):
    return self.hour

  def minute(self):
    return minute
