import requests

def fetch_shodan_data(api_key, ip_address):
    """Fetch open ports and vulnerabilities data from Shodan API."""
    url = f"https://api.shodan.io/shodan/host/{ip_address}?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

def fetch_ipinfo_data(api_key, ip_address):
    """Fetch IP details from IPinfo API."""
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
    response = requests.get(url)
    
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

SHODAN_API_KEY = "your_shodan_api_key"
IPINFO_API_KEY = "4acd9b2bc76c26"
VT_API_KEY = "cef813e5aaab3072239ebb5dc17e0a8ae2e6ad0c1f56137cc70bc9fce7a22109"
IP_ADDRESS = "8.8.8.8"

data_shodan = fetch_shodan_data(SHODAN_API_KEY, IP_ADDRESS)
data_ipinfo = fetch_ipinfo_data(IPINFO_API_KEY, IP_ADDRESS)
data_vt = fetch_virus_total_data(VT_API_KEY, IP_ADDRESS)

print("Shodan Data:", data_shodan)
print("IPinfo Data:", data_ipinfo)
print("VirusTotal Data:", data_vt)
