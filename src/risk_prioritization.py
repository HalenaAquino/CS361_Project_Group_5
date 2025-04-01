def calculate_weighted_score(likelihood, impact):
    """
    Calculates a weighted risk score.
    
    :param likelihood: Likelihood of the threat occurring (1-5).
    :param impact: Impact severity of the threat (1-5).
    :return: Weighted risk score.
    """
    return likelihood * impact

def prioritize_risks(threats):
    """
    Sorts threats by weighted risk score.
    
    :param threats: List of dictionaries, each containing 'name', 'likelihood', and 'impact'.
    :return: Sorted list of threats from highest to lowest risk.
    """
    for threat in threats:
        threat["risk_score"] = calculate_weighted_score(threat["likelihood"], threat["impact"])

    return sorted(threats, key=lambda x: x["risk_score"], reverse=True)
  
threats = [
    {"name": "SQL Injection", "likelihood": 4, "impact": 5},
    {"name": "Phishing", "likelihood": 5, "impact": 4},
    {"name": "DDoS", "likelihood": 3, "impact": 5}
]

top_threats = prioritize_risks(threats)

for threat in top_threats:
    print(f"Threat: {threat['name']}, Weighted Risk Score: {threat['risk_score']}")
