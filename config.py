import os

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

if not VIRUSTOTAL_API_KEY:
    VIRUSTOTAL_API_KEY = input("[!] Enter your VirusTotal API Key (optional, press Enter to skip): ")