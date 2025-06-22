import requests
from config import VIRUSTOTAL_API_KEY

def check_ip_reputation(ip):
    if not VIRUSTOTAL_API_KEY:
        return "API key not set"
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            return data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})
        else:
            return f"Error {resp.status_code}"
    except Exception as e:
        return f"Request failed: {e}"