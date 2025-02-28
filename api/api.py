import requests

def fetch_shodan_data(api_key, ip_address):
    """Fetch open ports and vulnerabilities data from Shodan API."""
    url = f"https://api.shodan.io/shodan/host/{ip_address}?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

def fetch_hibp_data(api_key, email):
    """Check if an email has been exposed in a data breach using Have I Been Pwned API."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": api_key, "User-Agent": "OSINT-Script"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

def fetch_virus_total_data(api_key, ip_address):
    """Fetch threat intelligence data from VirusTotal API."""
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"x-apikey": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

# Example usage
SHODAN_API_KEY = "your_shodan_api_key"
HIBP_API_KEY = "your_hibp_api_key"
VT_API_KEY = "your_virustotal_api_key"
IP_ADDRESS = "8.8.8.8"
EMAIL = "test@example.com"

data_shodan = fetch_shodan_data(SHODAN_API_KEY, IP_ADDRESS)
data_hibp = fetch_hibp_data(HIBP_API_KEY, EMAIL)
data_vt = fetch_virus_total_data(VT_API_KEY, IP_ADDRESS)

print("Shodan Data:", data_shodan)
print("Have I Been Pwned Data:", data_hibp)
print("VirusTotal Data:", data_vt)
