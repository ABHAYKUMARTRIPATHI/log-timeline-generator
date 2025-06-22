from dateutil import parser as dateparser

def parse_windows_logs(filepath):
    events = []
    with open(filepath, "r") as f:
        for line in f:
            try:
                parts = line.strip().split(",", 1)
                timestamp = dateparser.parse(parts[0])
                message = parts[1]
                events.append({"timestamp": timestamp, "message": message})
            except:
                continue
    return events