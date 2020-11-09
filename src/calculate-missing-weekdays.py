#!/usr/bin/env python3

import os
import datetime
import argparse
import ingest, helpers 


def fileChoices(choices, fileName, argParser):
    ext = os.path.splitext(fileName)[1][1:]
    if ext not in choices:
       argParser.error("file doesn't end with one of {}".format(choices))
    return fileName


def main():
    parser = argparse.ArgumentParser(description='Given a list of date intervals, find the missing weekdays for a given year')

    parser.add_argument('year')
    parser.add_argument('file', type=lambda s:fileChoices(('json', 'csv'), s, parser), help='either a JSON or CSV file')

    args = parser.parse_args()

    
    fileType = os.path.splitext(args.file)[1][1:]

    if fileType == 'json':
        intervals = ingest.json.jsonFileToObjectModel(args.file)
    elif fileType == 'csv':
        intervals = ingest.csv.csvFileToObjectModel(args.file)
    else:
        # file not supported
        print('file not supported')
        sys.exit(1)
    
    year = int(args.year)
    startDate = datetime.date(year, 1, 1)
    endDate = datetime.date(year, 12, 31)

    missingWeekdays = helpers.calculateMissingWeekdays(startDate, endDate, intervals)
    for date in missingWeekdays:
        print(date)

if __name__ == '__main__':
    main()