Class light:
  def name(self):
    return self.name

  def daily_time_on(self):
    return daily_time_on

  def daily_time_off(self):
    return daily_time_off(self)
  
  #TODO
  def is_on(self):
    return true

  def reason_for_last_change(self):
    return self.reason

  #TODO
  def turn_on(self, reason):
    return 

  #TODO
  def turn_off(self, reason):
    return 

  def should_be_on(self):
    return false 

  def __init__(name, daily_time_on, daily_time_off):
    self.name = name
    self.daily_time_on = daily_time_on
    self.daily_time_off = daily_time_off
    #TODO
    self.reason = 0
