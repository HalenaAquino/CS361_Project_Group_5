import openai
import os

# Set your OpenAI API key here or ensure it's set in your environment
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")  # Replace "your-api-key-here" if not using env variable

def predict_threat_behavior(threat_description):
    """
    Uses GPT-4 to analyze a described security threat and predict
    possible next attack vectors or behaviors.
    """
    prompt = f"Analyze this security threat and predict possible next attack vectors: {threat_description}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    threat = "SQL Injection detected on login page"
    prediction = predict_threat_behavior(threat)
    print(f"Predicted Next Steps: {prediction}")
