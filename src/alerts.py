import smtplib
import requests
from email.mime.text import MIMEText
import sqlite3
from datetime import datetime

# Database configuration - assuming SQLite for simplicity
DB_PATH = "/db/alerts.sql"

def initialize_database():
    """Create the alert_logs table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # You would typically run the alerts.sql script here
    # For this implementation, we're creating the table directly
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alert_logs (
        alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
        threat_name VARCHAR(255) NOT NULL,
        risk_score INTEGER NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        alert_message TEXT NOT NULL,
        recipient_email VARCHAR(255),
        notification_type VARCHAR(50) NOT NULL,
        status VARCHAR(50) NOT NULL,
        error_message TEXT,
        webhook_url VARCHAR(255),
        response_code INTEGER,
        response_message TEXT
    );
    ''')
    
    conn.commit()
    conn.close()

def log_alert(threat, risk_score, alert_message, notification_type, status, 
              recipient_email=None, error_message=None, webhook_url=None, 
              response_code=None, response_message=None):
    """Store alert logs in the database for future reference"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO alert_logs (
        threat_name, risk_score, alert_message, recipient_email, notification_type, 
        status, error_message, webhook_url, response_code, response_message
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        threat, risk_score, alert_message, recipient_email, notification_type,
        status, error_message, webhook_url, response_code, response_message
    ))
    
    conn.commit()
    conn.close()

def send_email_alert(threat, risk_score, recipient_email):
    """Send email alerts for high-risk threats (Risk Score > 20)"""
    if risk_score <= 20:
        return  # No alert needed
    
    alert_message = f"High-Risk Threat Detected: {threat} with Risk Score {risk_score}"
    msg = MIMEText(alert_message)
    msg["Subject"] = "Critical Cybersecurity Alert"
    msg["From"] = "alerts@shopsmart.com"
    msg["To"] = recipient_email
    
    try:
        with smtplib.SMTP("smtp.your-email.com", 587) as server:
            server.starttls()
            server.login("your-email", "your-password")
            server.sendmail("alerts@shopsmart.com", recipient_email, msg.as_string())
        print(f"Email alert sent successfully to {recipient_email}")
        
        # Log successful email alert
        log_alert(
            threat=threat,
            risk_score=risk_score,
            alert_message=alert_message,
            notification_type="email",
            status="sent",
            recipient_email=recipient_email
        )
        
        return True
    except Exception as e:
        error_message = f"Failed to send email alert: {e}"
        print(error_message)
        
        # Log failed email alert
        log_alert(
            threat=threat,
            risk_score=risk_score,
            alert_message=alert_message,
            notification_type="email",
            status="failed",
            recipient_email=recipient_email,
            error_message=str(e)
        )
        
        return False

def send_webhook_alert(threat, risk_score, webhook_url):
    """Send webhook alerts for high-risk threats (Risk Score > 20)"""
    if risk_score <= 20:
        return  # No alert needed
    
    alert_message = f"High-Risk Threat Detected: {threat} with Risk Score {risk_score}"
    payload = {
        "threat": threat,
        "risk_score": risk_score,
        "alert_type": "high_risk",
        "message": alert_message,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Raises exception for 4XX/5XX responses
        print(f"Webhook alert sent successfully to {webhook_url}")
        
        # Log successful webhook alert
        log_alert(
            threat=threat,
            risk_score=risk_score,
            alert_message=alert_message,
            notification_type="webhook",
            status="sent",
            webhook_url=webhook_url,
            response_code=response.status_code,
            response_message=response.text
        )
        
        return True
    except Exception as e:
        error_message = f"Failed to send webhook alert: {e}"
        print(error_message)
        
        # Get response code if available
        response_code = None
        if hasattr(e, 'response') and hasattr(e.response, 'status_code'):
            response_code = e.response.status_code
        
        # Log failed webhook alert
        log_alert(
            threat=threat,
            risk_score=risk_score,
            alert_message=alert_message,
            notification_type="webhook",
            status="failed",
            webhook_url=webhook_url,
            error_message=str(e),
            response_code=response_code
        )
        
        return False

if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Example threat list with risk scores
    threat_list = {
        "SQL Injection Attack": 21,
        "Lack of employee IS education": 15,
        "Physical breach": 15,
        "DDoS Attack": 16, 
        "Insecurely stored passwords": 20,
        "Lack of MFA": 15,
        "Lack of backups": 15,
        "E-commerce platform going down": 12,
        "Employee mistakes or lack of training": 10,
        "Payment processing going down": 12,
        "Excessive privileges": 16,
        "Weak encryption of customer records": 15,
        "Outdated firmware": 12,
        "Website defacement": 4,
        "Data leak": 15,
        "Man in the Middle Attack": 10,
        "Ransomware Attack": 25,
        "Zero-day Exploit": 22
    }
    
    email_recipient = "admin@shopsmart.com"
    webhook_url = "https://your-webhook-url.com/security-alerts"
    
    # Send alerts for each threat
    for threat, risk_score in threat_list.items():
        print(f"Processing: {threat} (Risk Score: {risk_score})")
        
        # Only send alerts for high-risk threats (Risk Score > 20)
        if risk_score > 20:
            send_email_alert(threat, risk_score, email_recipient)
            send_webhook_alert(threat, risk_score, webhook_url)
