class Range:
    def min(self):
        return self.min

    def max(self):
        return self.max

    def is_within_bounds(self, maybe):
        return self.compare_to(maybe) == 0

    def compare_to(self, to_check):
        if to_check < self.get_min():
            return -1
        if to_check > self.get_max():
            return 1
        return 0

    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
