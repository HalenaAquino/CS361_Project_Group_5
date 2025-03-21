import requests
import mysql.connector
import json
import os

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "bJhmxTVyiypZZ4X2RllTguMwB9ooR2JJ")
IPINFO_API_KEY = os.getenv("IPINFO_API_KEY", "4acd9b2bc76c26")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "cef813e5aaab3072239ebb5dc17e0a8ae2e6ad0c1f56137cc70bc9fce7a22109")

# Database connection parameters
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "threat_intel",
}

def store_data(source, ip, data):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO threat_data (source, ip_address, data) VALUES (%s, %s, %s)"
        cursor.execute(query, (source, ip, json.dumps(data)))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Stored {source} data for IP: {ip}")
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")

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
