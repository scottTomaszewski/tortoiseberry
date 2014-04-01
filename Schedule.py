import AttrDict

class Schedule:
  def __init__(self):
    self.taskList = []

  def tasks(self):
    return self.taskList

  def add(self, action, day, hour, minute):
    self.taskList.append(AttrDict.AttrDict({'action' : action, 'day' : day, 'hour' : hour, 'minute' : minute}))
