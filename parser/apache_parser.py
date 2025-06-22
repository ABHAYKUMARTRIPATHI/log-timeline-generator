from dateutil import parser as dateparser
import re

def parse_apache_logs(filepath):
    pattern = re.compile(r'\[(.*?)\] (.*)')
    events = []
    with open(filepath, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                timestamp = dateparser.parse(match.group(1))
                events.append({"timestamp": timestamp, "message": match.group(2)})
    return events