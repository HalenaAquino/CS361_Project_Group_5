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
    {"threat": "SQL Injection", "likelihood": random.randint(1, 5), "impact": random.randint(1, 5)},
    {"threat": "Phishing Attack", "likelihood": random.randint(1, 5), "impact": random.randint(1, 5)},
]

for threat in threats:
    base_risk_score = calculate_risk(threat["likelihood"], threat["impact"])
    refined_risk_score = refine_risk_score(threat["threat"], threat["likelihood"], threat["impact"])
    
    print(f"Threat: {threat['threat']}, Base Risk Score: {base_risk_score}, Refined Risk Score: {refined_risk_score}")
