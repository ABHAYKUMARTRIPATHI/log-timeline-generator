import os
from parser.apache_parser import parse_apache_logs
from parser.syslog_parser import parse_syslog_logs
from parser.windows_parser import parse_windows_logs
from utils.api_checker import check_ip_reputation

def select_parser():
    print("\n[1] Apache Logs\n[2] Syslog\n[3] Windows Logs")
    choice = input("Select log format: ")
    return {
        "1": parse_apache_logs,
        "2": parse_syslog_logs,
        "3": parse_windows_logs
    }.get(choice)

def apply_filters(events):
    keyword = input("Filter by keyword (press Enter to skip): ").strip()
    if keyword:
        events = [e for e in events if keyword.lower() in e['message'].lower()]
    return events

def main():
    log_path = input("Enter path to log file (e.g., logs/sample.log): ").strip()
    if not os.path.exists(log_path):
        print("[-] File not found.")
        return

    parser = select_parser()
    if not parser:
        print("[-] Invalid option.")
        return

    events = parser(log_path)
    if not events:
        print("[-] No events found.")
        return

    events = apply_filters(events)
    
    check_ips = input("Do you want to check IP reputations in log? (y/n): ").strip().lower()
    if check_ips == "y":
        for event in events:
            words = event['message'].split()
            for word in words:
                if "." in word and word.count(".") == 3:
                    result = check_ip_reputation(word)
                    event['message'] += f" | VT Check: {result}"

    output_path = "output/timeline_output.txt"
    with open(output_path, "w") as f:
        for e in sorted(events, key=lambda x: x['timestamp']):
            f.write(f"{e['timestamp']} - {e['message']}\n")

    print(f"[+] Timeline generated: {output_path}")

if __name__ == "__main__":
    main()