import json
from display import summary

# This file is meant for backup use, in the case that the json file saves but the log files don't for whatever reason.
# Also was used for testing and streamlining.

with open("raw_data.json", "r") as file:
    to_parse = json.load(file)

top5system = sorted(to_parse, key=lambda x: x[3])[0:10]
top5operation = sorted(to_parse, key=lambda x: x[4])[0:10]
logtext = ""
logtext += summary(top5system, "Top ten with regards to system cost")
logtext += summary(top5operation, "Top ten with regards to operation cost")

with open("logs/latest_json_parse.log", "w") as file:
    file.write(logtext)
