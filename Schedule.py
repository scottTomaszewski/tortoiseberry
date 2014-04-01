class Schedule:
  def __init__(self):
    self.tasks = []

  def tasks(self):
    return self.tasks

  def add(self, action, day, hour, minute):
    self.tasks.append({'action' : action, 'day' : day, 'hour' : hour, 'minute' : minute})
