# Final System Demonstration

## 1. Introduction to the Demonstration

Our project, the Real-Time Threat Intelligence (RTTI) platform, is designed to automate the process of detecting external threats, assessing their risk to our assets, and enabling immediate defensive actions.  
This system continuously pulls OSINT threat data, scores it using an AI risk model, maps it to our organizational assets, and displays it in real time on a secure dashboard, empowering blue teams to act proactively.

## 2. Real-Time Threat Intelligence Capabilities

The first major feature is our real-time threat intelligence ingestion.  
Using Python scripts like `fetch_osint.py` and `osint_integration.py`, our backend automatically queries sources like Shodan, VirusTotal, and IPinfo every hour.  
The threat information is processed, scored, and stored securely in our PostgreSQL database.

Each threat is assigned a risk score through TVA mapping and enhanced risk evaluation using GPT-4 via the `LLM_risk_analysis.py` module.  
This ensures every incoming threat is contextualized and prioritized intelligently.

![Screenshot 2025-04-27 163143](https://github.com/user-attachments/assets/80b6f16b-e685-448f-964f-72d556bbc5d8)


## 3. Blue Team Defense Mechanisms in Action

The live dashboard, built in React.js (`Dashboard.js`), visualizes all incoming threats against internal assets.  
Threats are sorted by risk score, with the highest-priority risks clearly highlighted for immediate action.

When a threat's risk score exceeds the predefined threshold (e.g., score > 20), our `alerts.py` script triggers automated alerts.  
These alerts are sent via SMTP email and optionally via webhook to external systems for incident response activation.

Additionally, our `blue_team_defense.py` script is set up to automatically block malicious IPs via firewall rules, providing an extra layer of automated protection.  

## 4. Risk Assessment and Automated Mitigation

Our risk assessment process involves two layers:  
- Baseline risk is calculated using likelihood × impact ratings based on asset criticality and threat severity.  
- Enhanced risk scoring is performed through GPT-4's contextual understanding, allowing a more dynamic and intelligent prioritization of threats.

Automated mitigation occurs immediately upon high-risk detection.  
Alerts are triggered without human intervention, reducing mean time to response and allowing defenders to act quickly.

## 5. Real-World Applications

The RTTI platform offers strong real-world applications across different organizational scales:

- **Corporate Networks**: Proactively monitor exposed assets for new vulnerabilities or unauthorized access.  
- **Cloud Security**: Detect and respond to misconfigured or exposed cloud services automatically.  
- **Small-to-Medium Businesses (SMBs)**: Enable proactive threat detection without needing a full Security Operations Center (SOC).  
- **Future Integrations**: Expand to dark web monitoring and direct SIEM (Splunk, ELK) integrations for larger organizations.

By automating threat intelligence, contextualizing it, and triggering rapid alerts, RTTI dramatically improves an organization’s security posture and response time.
