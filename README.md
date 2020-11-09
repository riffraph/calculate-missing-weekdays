# calculate-missing-weekdays

given a list of date intervals, find the missing weekdays for a given year

runtime: Python 3.6

## how to run
`calculate-missing-weekdays.py <b>[year]</b> <b>[file]</b>`

e.g. <i>calculate-missing-weekdays.py 2020 intervals.json</i>

## Input

* year: a calendar year
* file: a CSV or JSON file with date intervals
  
### CSV file example

the first column is the start and the second column is the end.

```
1-1-2020,20-1-2020
6-4-2020,20-4-2020
```

### JSON file example

```
{
    "intervals": [ 
        { "start":  "1-1-2020", "end": "20-1-2020"}, 
        { "start":  "6-4-2020", "end": "20-4-2020"} 
        ] 
}    
```

## Output
a list of dates which are missing and are weekdays

### Assumptions
* the routine assumes that intervals are sorted and do not overlap



