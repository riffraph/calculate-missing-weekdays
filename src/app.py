#!/usr/bin/env python3

import sys
import json
import datetime
import model, calculate


def jsonToObjectModel(intervalCollection):
    # expecting a collection (dictionary) of json objects
    result = []

    for node in intervalCollection:
        start = datetime.datetime.strptime(node['start'], '%d-%m-%Y').date()
        end = datetime.datetime.strptime(node['end'], '%d-%m-%Y').date()
        result.append(model.Interval(start, end))
        
    return result

def main():
    year = int(sys.argv[1])
    inFile = sys.argv[2]

    startDate = datetime.date(year, 1, 1)
    endDate = datetime.date(year, 12, 31)

    with open(inFile, 'r') as f:
        intervals_dict = json.load(f)

    # expecting a json node with key 'intervals'
    # this should have an array of objects, where each object represents a date interval
    intervals = jsonToObjectModel(intervals_dict['intervals'])
    missingWeekdays = calculate.helpers.calculateMissingWeekdays(startDate, endDate, intervals)
    for date in missingWeekdays:
        print(date)

if __name__ == '__main__':
    main()