import datetime
import sqlite3

# Response plans for known threats
def incident_response(threat):
    response_plan = {
        "SQL Injection": "1. Block the attacking IP. 2. Patch the vulnerability. 3. Conduct forensic analysis.",
        "Phishing": "1. Notify affected users. 2. Change compromised credentials. 3. Update phishing filters.",
        "DDoS Attack": "1. Activate DDoS mitigation. 2. Enable rate limiting. 3. Monitor ongoing traffic.",
        "Ransomware": "1. Isolate affected systems. 2. Restore from backups. 3. Conduct forensic investigation.",
        "Malware": "1. Quarantine infected machines. 2. Run full system scans. 3. Update security software."
    }
    return response_plan.get(threat, "No response plan available.")

# Mitigation strategies for each threat
def mitigation_strategy(threat):
    strategies = {
        "SQL Injection": "Use parameterized queries and enable a WAF.",
        "Phishing": "Enable 2FA and educate users on phishing recognition.",
        "DDoS Attack": "Use DDoS protection services and implement rate limiting.",
        "Ransomware": "Maintain regular offline backups and isolate infected systems.",
        "Malware": "Keep antivirus updated and perform regular scans."
    }
    return strategies.get(threat, "No mitigation strategy available.")

# Log incident to the database
def log_incident(threat, status="Detected"):
    conn = sqlite3.connect("incident_logs.db")
    cursor = conn.cursor()

    # Create table with status enforcement and mitigation column
    cursor.execute('''CREATE TABLE IF NOT EXISTS incident_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        threat_name TEXT,
                        response TEXT,
                        mitigation TEXT,
                        timestamp TEXT,
                        status TEXT CHECK(status IN ('Detected', 'In Progress', 'Resolved')) NOT NULL)''')

    response = incident_response(threat)
    mitigation = mitigation_strategy(threat)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO incident_logs (threat_name, response, mitigation, timestamp, status) VALUES (?, ?, ?, ?, ?)", 
                   (threat, response, mitigation, timestamp, status))

    conn.commit()
    conn.close()

    return f"Incident logged: {threat} at {timestamp} with status '{status}'"
