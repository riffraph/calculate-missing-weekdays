# calculate-missing-weekdays

given a list of date intervals, find the missing weekdays for a calendar year

runtime: Python 3.6

### how to run
<i>python3 calculate-missing-periods.py [year] [file]</i>

<i>e.g. python3 calculate-missing-periods.py 2020 intervals.json</i>

### Input

* year: a calendar year
* file: a JSON file with date intervals, in the format like
{ "intervals": [ { "start":  "1-1-2020", "end": "20-1-2020"}, { "start":  "6-4-2020", "end": "20-4-2020"} ] }

### Output
a list of dates which are missing and are weekdays

#### Assumptions
* the routine assumes that intervals are sorted and do not overlap



