import datetime

class helpers:

    # generate a date range, excluding weekends
    @staticmethod
    def dateRange(start, end):
        for n in range(int((end - start).days)):
            if (start + datetime.timedelta(n)).weekday() < 5:
                yield start + datetime.timedelta(n)

    @staticmethod
    def isDateInAnInterval(date, intervalList):
        for interval in intervalList:
            if date >= interval.start and date <= interval.end:
                return True
            
        return False

    @staticmethod
    def calculateMissingWeekdays(startDate, endDate, intervals):
        result = []
        ## assume intervals are sorted and do not overlap
        # probably could be optimised, but assume the intervals cover a subset of the comparison period
        # scan each weekday of the comparison period, and test if is in a supplied interval
        for date in helpers.dateRange(startDate, endDate):
            if not helpers.isDateInAnInterval(date, intervals):
                result.append(date)

        return result
