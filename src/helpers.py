import datetime
import model


def calculateMissingWeekdays(startDate, endDate, intervals):
    result = []
    ## assume intervals are sorted and do not overlap
    # probably could be optimised, but assume the intervals cover a subset of the comparison period
    # scan each weekday of the comparison period, and test if is in a supplied interval
    for date in dateRange(startDate, endDate):
        if not isDateInAnInterval(date, intervals):
            result.append(date)

    return result

#class helpers:

# generate a date range, excluding weekends

def dateRange(start, end):
    for n in range(int((end - start).days)):
        if (start + datetime.timedelta(n)).weekday() < 5:
            yield start + datetime.timedelta(n)

# determine if a given date is in a given list of intervals
# an interval is an object with a start:Date and end:Date attributes

def isDateInAnInterval(date, intervalList):
    for interval in intervalList:
        if date >= interval.start and date <= interval.end:
            return True
        
    return False