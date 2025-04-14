# User Guide: Blue Team Analyst Manual

## Welcome

This guide supports blue team analysts in using the Threat Intelligence Dashboard for monitoring, investigation, and mitigation of cybersecurity threats.

## 1. Logging In

- Navigate to: `https://dashboard-url.com/login`
- Enter your credentials
- Complete two-factor authentication (2FA)

## 2. Dashboard Overview

### Key Panels
- **Live Threat Feed**: Displays recent alerts
- **Metrics Panel**: Shows summary stats
- **Search Bar**: Query by threat name, type, IP, or time

### Use Cases
- Identify new attacks
- Trace repeated threat actors
- Export data for reports

## 3. Investigating Threats

1. Go to **Threat Logs**
2. Click a threat to expand details:
   - Source IP
   - Type (e.g., malware, ransomware)
   - Severity Score
   - Timestamp
3. Actions:
   - Tag for review
   - Add notes
   - Export report

## 4. Using the Mitigation Center

### Automated Threat Actions
- Block suspicious IPs
- Quarantine affected nodes
- Run predefined remediation scripts

### Analyst Controls
- Review and approve/undo mitigations
- Add or remove from watchlists
- Trigger manual investigation

## 5. Best Practices

- Monitor live feed hourly during active shifts
- Use filters for triage (e.g., `severity >= 8`)
- Document decisions in threat logs
- Sync with threat intelligence updates weekly

## 6. Help & Support

- Visit `/docs/help.md` for common issues
- Email the SOC team: `security-team@org.com`
