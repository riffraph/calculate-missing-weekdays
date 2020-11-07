import sys
import json
from types import SimpleNamespace
import datetime

class Interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '--Interval: start={} - end={}'.format(self.start, self.end)


def isDateInAnInterval(date, intervalList):
    for interval in intervalList:
        if date >= interval.start and date <= interval.end:
            return True
        
    return False


def jsonToObjectModel(intervalCollection):
    # expecting a collection (dictionary) of json objects
    result = []

    for node in intervalCollection:
        start = datetime.datetime.strptime(node['start'], '%d-%m-%Y').date()
        end = datetime.datetime.strptime(node['end'], '%d-%m-%Y').date()
        result.append(Interval(start, end))
        
    return result

# generate a date range, excluding weekends
def dateRange(start, end):
    for n in range(int((end - start).days)):
        if (start + datetime.timedelta(n)).weekday() < 5:
            yield start + datetime.timedelta(n)

def main():
    year = int(sys.argv[1])
    inFile = sys.argv[2]

    compareStart = datetime.date(year, 1, 1)
    compareEnd = datetime.date(year, 12, 31)
    
    with open(inFile, 'r') as f:
        intervals_dict = json.load(f)

    # algorithm
    ## assume intervals are sorted and do not overlap
    # probably could be optimised, but assume the intervals cover a subset of the comparison period
    # scan each weekday of the comparison period, and test if is in a supplied interval

    # expecting a json node with key 'intervals'
    # this should have an array of objects, where each object represents a date interval
    suppliedIntervals = jsonToObjectModel(intervals_dict['intervals'])

    for date in dateRange(compareStart, compareEnd):
        if not isDateInAnInterval(date, suppliedIntervals):
            print(date)
            

if __name__ == '__main__':
    main()