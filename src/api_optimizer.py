import redis
import requests
import json

# Redis setup
cache = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# OSINT API endpoint (replace with actual API)
OSINT_API_URL = "https://api.osint-threats.com/getThreatInfo"

def fetch_from_osint(ip):
    """Fetch threat data from OSINT API."""
    response = requests.get(f"{OSINT_API_URL}?ip={ip}")
    return response.json() if response.status_code == 200 else {}

def get_threat_data(ip):
    """Retrieve threat data with caching."""
    cached_data = cache.get(ip)
    
    if cached_data:
        print("Cache hit: Returning cached data")
        return json.loads(cached_data)  # Convert from string to dictionary
    else:
        print("Cache miss: Fetching from API")
        data = fetch_from_osint(ip)
        
        if data:
            cache.setex(ip, 3600, json.dumps(data))  # Cache for 1 hour (3600 sec)
        
        return data

# Example Usage
if __name__ == "__main__":
    ip_address = "192.168.1.100"
    threat_info = get_threat_data(ip_address)
    print("Threat Intelligence Data:", threat_info)
