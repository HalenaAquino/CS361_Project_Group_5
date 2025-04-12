def automated_response(threat):
    responses = {
        "DDoS Attack": "Activate rate limiting and blackhole routing.",
        "Lack of employee IS education": "Initiate company-wide cybersecurity awareness training.",
        "Physical breach": "Trigger facility lockdown and alert physical security team.",
        "SQL Injection": "Apply Web Application Firewall (WAF) rules.",
        "Insecurely stored passwords": "Enforce secure hashing (bcrypt/Argon2) and password vault policies.",
        "Lack of MFA": "Require multi-factor authentication for all user accounts.",
        "Lack of backups": "Start immediate backup job and verify recovery points.",
        "E-commerce platform going down": "Switch to high-availability backup instance.",
        "Employee mistakes or lack of training": "Log incident and prompt just-in-time security training.",
        "Payment processing going down": "Redirect to alternate payment gateway and notify operations.",
        "Excessive privileges": "Enforce least privilege by revoking unnecessary access.",
        "Weak encryption of customer records": "Upgrade to AES-256 encryption and re-encrypt data.",
        "Outdated firmware": "Schedule urgent firmware updates across all devices.",
        "Website defacement": "Restore from clean backup and enable WAF.",
        "Data leak": "Isolate affected system and activate data breach response plan.",
        "Man in the Middle Attack": "Enforce TLS 1.3 and reissue certificates."
    }
    return responses.get(threat, "No automatic response available.")

# Example Usage
if __name__ == "__main__":
    action = automated_response("SQL Injection")
    print(f"Recommended Action: {action}")
