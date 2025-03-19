import smtplib
from email.mime.text import MIMEText

def send_email_alert(threat, risk_score, recipient_email):
    if risk_score <= 20:
        return  # No alert needed

    msg = MIMEText(f"High-Risk Threat Detected: {threat} with Risk Score {risk_score}")
    msg["Subject"] = "Critical Cybersecurity Alert"
    msg["From"] = "alerts@shopsmart.com"
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.your-email.com", 587) as server:
            server.starttls()
            server.login("your-email", "your-password")
            server.sendmail("alerts@shopsmart.com", recipient_email, msg.as_string())
        print(f"Email alert sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Example usage
if __name__ == "__main__":
    threat_list = {
        "SQL Injection Attack": 20,
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
        "Man in the Middle Attack": 10
    }
    
    email_recipient = "admin@shopsmart.com"
    
    for threat, risk_score in threat_list.items():
        send_email_alert(threat, risk_score, email_recipient)

