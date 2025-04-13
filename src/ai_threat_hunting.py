import openai
import os
import pandas as pd  # For basic log analysis (can be expanded)
from sklearn.ensemble import IsolationForest # example ML model

# Set your OpenAI API key here or ensure it's set in your environment
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")  # Replace "your-api-key-here" if not using env variable

def predict_threat_behavior(threat_description):
    """
    Uses GPT-4 to analyze a described security threat and predict
    possible next attack vectors or behaviors.
    """
    prompt = f"Analyze this security threat and predict possible next attack vectors and behaviors, also provide a short list of mitigation recommendations: {threat_description}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity analyst. Provide detailed analysis and mitigation steps."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def analyze_network_logs(network_logs_str):
    """
    Analyzes network logs for anomalies using GPT-4 and basic ML anomaly detection.
    """
    try:
        df = pd.read_csv(pd.compat.StringIO(network_logs_str)) # creates a dataframe from the string.
        if 'Bytes' in df.columns:
            model = IsolationForest(contamination=0.05) # 5% anomalies
            model.fit(df[['Bytes']])
            df['anomaly'] = model.predict(df[['Bytes']])
            anomalies = df[df['anomaly'] == -1]
            if not anomalies.empty:
              print("Network log Anomaly Detected:")
              print(anomalies)

        prompt = f"Analyze these network logs for potential security anomalies: {network_logs_str}. Identify any suspicious patterns or activities, and suggest possible threat vectors."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a network security analyst. Identify anomalies and potential security threats."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"

def analyze_user_behavior(user_behavior_logs):
    """
    Analyzes user behavior logs for anomalies using GPT-4.
    """
    prompt = f"Analyze these user behavior logs for potential security anomalies: {user_behavior_logs}. Identify any unusual or suspicious activities."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a user behavior security analyst. Identify anomalies and potential insider threats."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def analyze_file_integrity(file_integrity_logs):
    """
    Analyzes file integrity logs for anomalies using GPT-4.
    """
    prompt = f"Analyze these file integrity logs for potential security anomalies: {file_integrity_logs}. Identify any unexpected changes or modifications."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a file integrity monitoring analyst. Identify unauthorized changes."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def analyze_system_logs(system_logs):
    """
    Analyzes system logs for anomalies using GPT-4.
    """
    prompt = f"Analyze these system logs for potential security anomalies: {system_logs}. Identify any unexpected errors or events."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a system log analysis expert. Identify abnormal logs."},
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
    print(f"Predicted Next Steps: {prediction}\n")

    network_logs = """
    Timestamp,Source IP,Destination IP,Port,Protocol,Bytes
    2023-10-26 10:00:00,192.168.1.10,192.168.1.100,80,TCP,1024
    2023-10-26 10:01:00,192.168.1.11,192.168.1.100,443,TCP,2048
    2023-10-26 10:02:00,192.168.1.12,192.168.1.100,22,TCP,512
    2023-10-26 10:03:00,192.168.1.10,192.168.1.200,8080,TCP,4096
    2023-10-26 10:04:00,192.168.1.10,203.0.113.1,80,TCP,8192
    2023-10-26 10:05:00,192.168.1.10,192.168.1.100,80,TCP,1024
    2023-10-26 10:06:00,192.168.1.11,192.168.1.100,443,TCP,2048
    2023-10-26 10:07:00,192.168.1.12,192.168.1.100,22,TCP,512
    2023-10-26 10:08:00,192.168.1.10,192.168.1.200,8080,TCP,4096
    2023-10-26 10:09:00,192.168.1.10,203.0.113.1,80,TCP,8192
    2023-10-26 10:10:00,192.168.1.10,203.0.113.1,80,TCP,30000 # added an anomaly
    """
    network_analysis = analyze_network_logs(network_logs)
    print(f"Network Log Analysis: {network_analysis}\n")

    user_behavior_logs = """
    Timestamp,User ID,Action,Resource,Location
    2023-10-26 10:00:00,user1,login,dashboard,office
    2023-10-26 10:05:00,user1,download,report.pdf,office
    2023-10-26 10:10:00,user2,login,email,home
    2023-10-26 10:15:00,user2,send_email,confidential.doc,home
    2023-10-26 10:20:00,user3,login,database,remote
    2023-10-26 10:25:00,user3,query,sensitive_data,remote
    """
    user_analysis = analyze_user_behavior(user_behavior_logs)
    print(f"User Behavior Analysis: {user_analysis}\n")

    file_integrity_logs = """
    Timestamp,File Path,Action,User
    2023-10-26 10:00:00,/etc/passwd,modified,root
    2023-10-26 10:05:00,/var/log/auth.log,accessed,system
    2023-10-26 10:10:00,/home/user1/important.txt,modified,user1
    2023-10-26 10:15:00,/home/user2/config.ini,modified,user2
    """
    file_integrity_analysis = analyze_file_integrity(file_integrity_logs)
    print(f"File Integrity Analysis: {file_integrity_analysis}\n")

    system_logs = """
    Timestamp,Severity,Message
    2023-10-26 10:00:00,ERROR,Disk full
    2023-10-26 10:05:00,WARNING,Unusual network activity
    2023-10-26 10:10:00,INFO,System restart
    2023-10-26 10:15:00,CRITICAL,Memory allocation failure
    """
    system_analysis = analyze_system_logs(system_logs)
    print(f"System Log Analysis: {system_analysis}")
