import json as jsonLib
import csv as csvLib
import datetime
import model


class json:

    @staticmethod
    def jsonToObjectModel(intervalCollection):
        # expecting a collection (dictionary) of json objects
        result = []

        for node in intervalCollection:
            start = datetime.datetime.strptime(node['start'], '%d-%m-%Y').date()
            end = datetime.datetime.strptime(node['end'], '%d-%m-%Y').date()
            result.append(model.Interval(start, end))
            
        return result

    @staticmethod
    def jsonFileToObjectModel(inFile):
        intervals = []

        with open(inFile, 'r') as f:
            intervals_dict = jsonLib.load(f)

            # expecting a json node with key 'intervals'
            # this should have an array of objects, where each object represents a date interval
            intervals = json.jsonToObjectModel(intervals_dict['intervals'])

        return intervals


class csv:

    @staticmethod
    def csvFileToObjectModel(inFile):
        intervals = []

        with open(inFile, 'r') as f:
            reader = csvLib.reader(f, delimiter=",")
            for line in reader:
                start = datetime.datetime.strptime(line[0], '%d-%m-%Y').date()
                end = datetime.datetime.strptime(line[1], '%d-%m-%Y').date()
                intervals.append(model.Interval(start, end))
        
        return intervals