import openai  
import random  

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def calculate_risk(likelihood, impact):
    return likelihood * impact

def refine_risk_score(threat, likelihood, impact):
    prompt = f"Given a cybersecurity threat '{threat}', with a likelihood score of {likelihood} and an impact score of {impact}, how severe is the risk on a scale of 1-10? Provide a single numeric value."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    refined_score = response["choices"][0]["message"]["content"]
    
    try:
        return int(refined_score)
    except ValueError:
        return calculate_risk(likelihood, impact)  

threats = [
    {"threat": "DDoS Attack", "likelihood": 4, "impact": 2},
    {"threat": "Lack of employee IS education", "likelihood": 3, "impact": 4},
    {"threat": "Physical breach", "likelihood": 1, "impact": 5},
    {"threat": "SQL Injection", "likelihood": 4, "impact": 5},
    {"threat": "Insecurely stored passwords", "likelihood": 3, "impact": 4},
    {"threat": "Lack of MFA", "likelihood": 3, "impact": 4},
    {"threat": "Lack of backups", "likelihood": 2, "impact": 4},
    {"threat": "E-commerce platform going down", "likelihood": 3, "impact": 3},
    {"threat": "Employee mistakes or lack of training", "likelihood": 3, "impact": 3},
    {"threat": "Payment processing going down", "likelihood": 3, "impact": 3},
    {"threat": "Excessive privileges", "likelihood": 4, "impact": 5},
    {"threat": "Weak encryption of customer records", "likelihood": 3, "impact": 3},
    {"threat": "Outdated firmware", "likelihood": 3, "impact": 4},
    {"threat": "Website defacement", "likelihood": 3, "impact": 1},
    {"threat": "Data leak", "likelihood": 3, "impact": 4},
    {"threat": "Man in the Middle Attack", "likelihood": 2, "impact": 4},
]

for threat in threats:
    base_risk_score = calculate_risk(threat["likelihood"], threat["impact"])
    refined_risk_score = refine_risk_score(threat["threat"], threat["likelihood"], threat["impact"])
    
    print(f"Threat: {threat['threat']}, Base Risk Score: {base_risk_score}, Refined Risk Score: {refined_risk_score}")
