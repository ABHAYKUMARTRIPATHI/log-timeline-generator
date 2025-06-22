from dateutil import parser as dateparser

def parse_syslog_logs(filepath):
    events = []
    with open(filepath, "r") as f:
        for line in f:
            try:
                timestamp_str = ' '.join(line.split()[:3])
                timestamp = dateparser.parse(timestamp_str)
                message = ' '.join(line.split()[4:])
                events.append({"timestamp": timestamp, "message": message})
            except:
                continue
    return events