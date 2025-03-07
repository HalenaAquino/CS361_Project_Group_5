import requests
import psycopg2
import time
from datetime import datetime

# API Keys (Replace with your actual API keys)
SHODAN_API_KEY = "your_shodan_api_key"
HIBP_API_KEY = "your_hibp_api_key"
SECURITYTRAILS_API_KEY = "your_securitytrails_api_key"

# Target IP and domain (Modify as needed)
IP_ADDRESS = "8.8.8.8"
DOMAIN = "example.com"

# PostgreSQL Connection
DB_CONFIG = {
    "dbname": "threat_intel",
    "user": "admin",
    "password": "securepass",
    "host": "localhost",
    "port": "5432"
}

def store_data(threat_source, threat_data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO threat_data (timestamp, threat_source, data)
            VALUES (%s, %s, %s)
        """, (datetime.utcnow(), threat_source, threat_data))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Database error:", e)

def fetch_shodan():
    url = f"https://api.shodan.io/shodan/host/{IP_ADDRESS}?key={SHODAN_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        store_data("Shodan", response.json())

def fetch_hibp():
    headers = {"hibp-api-key": HIBP_API_KEY, "User-Agent": "ThreatIntelScript"}
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{DOMAIN}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        store_data("HIBP", response.json())

def fetch_securitytrails():
    url = f"https://api.securitytrails.com/v1/domain/{DOMAIN}?apikey={SECURITYTRAILS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        store_data("SecurityTrails", response.json())

def main():
    fetch_shodan()
    fetch_hibp()
    fetch_securitytrails()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)  # Runs every hour
