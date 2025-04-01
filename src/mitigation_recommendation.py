class RiskMitigation:
    def _init_(self):
        self.recommendations = {
            "SQL Injection": "Enable parameterized queries and use a Web Application Firewall (WAF).",
            "Phishing": "Enforce two-factor authentication and train employees on phishing awareness.",
            "DDoS": "Implement rate limiting and use DDoS protection services.",
            "Malware": "Use endpoint protection software and regularly update system patches.",
            "Privilege Escalation": "Enforce the principle of least privilege (PoLP) and monitor access logs.",
            "Zero-Day Exploit": "Apply security patches immediately and use an intrusion detection system (IDS)."
        }

    def recommend_mitigation(self, threat):
        return self.recommendations.get(threat, "No recommendation available.")

# Example usage
if _name_ == "_main_":
    mitigation_system = RiskMitigation()
    threat = "Phishing"
    mitigation = mitigation_system.recommend_mitigation(threat)
    print(f"Recommended Mitigation for {threat}: {mitigation}")
