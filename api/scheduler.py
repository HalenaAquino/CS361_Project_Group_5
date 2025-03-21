import schedule
import time
import sqlite3
import logging
from shodan_integration import fetch_shodan_data
from ipinfo_integration import fetch_ipinfo_data
from virustotal_integration import fetch_virustotal_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DB_NAME = "threat_intelligence.db"

def init_db():
    """Initialize database to store threat intelligence data."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS threat_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def store_data(source, data):
    """Store fetched threat intelligence data in the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO threat_data (source, data) VALUES (?, ?)", (source, str(data)))
    conn.commit()
    conn.close()
    logging.info(f"Stored {source} data in database.")

def run_osint_updates():
    
    logging.info("Fetching OSINT threat data...")
    
    try:
        shodan_data = fetch_shodan_data()
        store_data("Shodan", shodan_data)
    except Exception as e:
        logging.error(f"Error fetching Shodan data: {e}")

    try:
        ipinfo_data = fetch_ipinfo_data()
        store_data("IPInfo", ipinfo_data)
    except Exception as e:
        logging.error(f"Error fetching IPInfo data: {e}")

    try:
        virustotal_data = fetch_virustotal_data()
        store_data("VirusTotal", virustotal_data)
    except Exception as e:
        logging.error(f"Error fetching VirusTotal data: {e}")

    logging.info("Threat intelligence update completed.")

# Initialize the database
init_db()

# Schedule API calls every 6 hours
schedule.every(6).hours.do(run_osint_updates)

logging.info("Threat Intelligence Scheduler Started.")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  
