import datetime

# Function to calculate dynamic risk score based on likelihood, impact, and time decay
def calculate_risk(likelihood, impact, last_seen):
    """
    Calculate the risk score for a given threat based on its likelihood, impact, and how long it's been since it was last seen.
    
    Parameters:
    likelihood (int): Likelihood of the threat occurring (1 to 5).
    impact (int): Impact of the threat (1 to 5).
    last_seen (datetime): The date when the threat was last observed.
    
    Returns:
    float: The time-weighted risk score.
    """
    # Calculate the number of days since the threat was last observed
    days_since_last_seen = (datetime.datetime.now() - last_seen).days
    
    # Decay factor: reduces risk over time, but never goes below 0.1 (to ensure the threat still has some weight even if it's old)
    decay_factor = max(0.1, 1 - (0.05 * days_since_last_seen))
    
    # Calculate and return the risk score with decay factor applied
    risk_score = (likelihood * impact) * decay_factor
    return risk_score

# Example data: Threat with likelihood 4, impact 5, last seen on March 20, 2025
threat_last_seen = datetime.datetime(2025, 3, 20)

# Calculate the updated risk score for the given threat
risk_score = calculate_risk(4, 5, threat_last_seen)

# Print the calculated risk score
print(f"Updated Risk Score: {risk_score:.2f}")

# Example of using this for multiple threats
threats = [
    {'likelihood': 4, 'impact': 5, 'last_seen': datetime.datetime(2025, 3, 20)},
    {'likelihood': 3, 'impact': 4, 'last_seen': datetime.datetime(2025, 3, 1)},
    {'likelihood': 5, 'impact': 5, 'last_seen': datetime.datetime(2025, 4, 5)},
    {'likelihood': 2, 'impact': 3, 'last_seen': datetime.datetime(2025, 2, 15)}
]

# Calculate risk scores for all threats and print the results
for i, threat in enumerate(threats, start=1):
    risk_score = calculate_risk(threat['likelihood'], threat['impact'], threat['last_seen'])
    print(f"Threat {i} Risk Score: {risk_score:.2f}")
