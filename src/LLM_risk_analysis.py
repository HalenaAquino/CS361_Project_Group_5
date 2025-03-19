import openai

def analyze_risk(threat, likelihood, impact):
    prompt = f"Analyze the risk score for {threat} with likelihood {likelihood} and impact {impact}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# List of threats with their likelihood and impact
threats = [
    {"threat": "DDoS Attack", "likelihood": 4, "impact": 4},
    {"threat": "Lack of employee IS education", "likelihood": 5, "impact": 3},
    {"threat": "Physical breach", "likelihood": 3, "impact": 5},
    {"threat": "SQL Injection", "likelihood": 4, "impact": 5},
    {"threat": "Insecurely stored passwords", "likelihood": 5, "impact": 4},
    {"threat": "Lack of MFA", "likelihood": 5, "impact": 3},
    {"threat": "Lack of backups", "likelihood": 3, "impact": 5},
    {"threat": "E-commerce platform going down", "likelihood": 4, "impact": 3},
    {"threat": "Employee mistakes or lack of training", "likelihood": 5, "impact": 2},
    {"threat": "Payment processing going down", "likelihood": 3, "impact": 4},
    {"threat": "Excessive privileges", "likelihood": 4, "impact": 4},
    {"threat": "Weak encryption of customer records", "likelihood": 3, "impact": 5},
    {"threat": "Outdated firmware", "likelihood": 4, "impact": 3},
    {"threat": "Website defacement", "likelihood": 2, "impact": 2},
    {"threat": "Data leak", "likelihood": 3, "impact": 5},
    {"threat": "Man in the Middle Attack", "likelihood": 2, "impact": 5}
]

# Process all threats
def analyze_all_threats(threat_list):
    print("\nAnalyzing all threats:")
    print("-" * 50)
    
    # Sort threats by calculated risk score (likelihood * impact) in descending order
    sorted_threats = sorted(
        threat_list,
        key=lambda x: x["likelihood"] * x["impact"],
        reverse=True
    )
    
    results = []
    for threat_info in sorted_threats:
        # Calculate basic risk score
        basic_score = threat_info["likelihood"] * threat_info["impact"]
        
        # Get AI assessment
        ai_assessment = analyze_risk(
            threat_info["threat"], 
            threat_info["likelihood"], 
            threat_info["impact"]
        )
        
        # Store results
        results.append({
            "threat": threat_info["threat"],
            "likelihood": threat_info["likelihood"],
            "impact": threat_info["impact"],
            "basic_score": basic_score,
            "ai_assessment": ai_assessment
        })
        
        # Print result
        print(f"\nThreat: {threat_info['threat']}")
        print(f"Likelihood: {threat_info['likelihood']}, Impact: {threat_info['impact']}")
        print(f"Our Risk Score: {basic_score}")
        print(f"AI Assessment: {ai_assessment}")
        print("-" * 50)
    
    return results

all_results = analyze_all_threats(threats)
