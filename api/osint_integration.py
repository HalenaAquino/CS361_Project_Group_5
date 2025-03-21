import requests
import psycopg2
import json
import os

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "your_shodan_api_key")
IPINFO_API_KEY = os.getenv("IPINFO_API_KEY", "your_ipinfo_api_key")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "your_virustotal_api_key")

DB_CONFIG = {
    "dbname": "threat_intel",
    "user": "admin",
    "password": "securepass",
    "host": "localhost",
    "port": "5432",
}

def store_data(source, ip, data):
    """Store threat intelligence data in PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO threat_data (source, ip_address, data) VALUES (%s, %s, %s)",
            (source, ip, json.dumps(data)),
        )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Stored {source} data for IP: {ip}")
    except Exception as e:
        print(f"Database error: {e}")

def fetch_shodan_data(ip):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        store_data("Shodan", ip, data)
        return data
    else:
        print(f"Shodan API error: {response.text}")
        return None

def fetch_ipinfo_data(ip):
    url = f"https://ipinfo.io/{ip}/json?token={IPINFO_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        store_data("IPInfo", ip, data)
        return data
    else:
        print(f"IPInfo API error: {response.text}")
        return None

def fetch_virustotal_data(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        store_data("VirusTotal", ip, data)
        return data
    else:
        print(f"VirusTotal API error: {response.text}")
        return None

def run_osint_scan(ip):
    print(f"Scanning IP: {ip}")
    fetch_shodan_data(ip)
    fetch_ipinfo_data(ip)
    fetch_virustotal_data(ip)

if __name__ == "__main__":
    test_ip = "8.8.8.8"
    run_osint_scan(test_ip)
