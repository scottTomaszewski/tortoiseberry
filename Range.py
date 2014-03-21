class range:
  def min(self):
    return self.min

  def max(self):
    return self.max

  def is_within_bounds(self, maybe):
    return self.compare_to(maybe) == 0

  def compare_to(self, toCheck):
    if toCheck < self.get_min():
      return -1
    if toCheck > self.get_max():
      return 1
    return 0

  def __init__(min, max):
    self.min = min
    self.max = max
