class Interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '--Interval: start={} - end={}'.format(self.start, self.end)
