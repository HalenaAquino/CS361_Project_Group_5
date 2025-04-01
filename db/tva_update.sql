-- TVA Mapping Update Script
ttva_update.sql

-- Updating likelihood based on OSINT threat intelligence
    
UPDATE tva_mapping
SET likelihood = CASE
    WHEN threat_name = 'Phishing' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'Phishing' 
        AND threat_data.risk_score > 20
    ) THEN 5
    WHEN threat_name = 'Malware' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'Malware' 
        AND threat_data.risk_score > 30
    ) THEN 4
    WHEN threat_name = 'Ransomware' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'Ransomware' 
        AND threat_data.risk_score > 40
    ) THEN 5
    WHEN threat_name = 'DDoS Attack' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'DDoS Attack' 
        AND threat_data.risk_score > 25
    ) THEN 4
    WHEN threat_name = 'SQL Injection' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'SQL Injection' 
        AND threat_data.risk_score > 35
    ) THEN 5
    ELSE likelihood
END;

-- Adjusting impact values based on evolving threat intelligence

UPDATE tva_mapping
SET impact = CASE
    WHEN threat_name = 'Phishing' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'Phishing' 
        AND threat_data.risk_score > 25
    ) THEN 4
    WHEN threat_name = 'Malware' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'Malware' 
        AND threat_data.risk_score > 35
    ) THEN 5
    WHEN threat_name = 'Ransomware' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'Ransomware' 
        AND threat_data.risk_score > 45
    ) THEN 5
    WHEN threat_name = 'DDoS Attack' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'DDoS Attack' 
        AND threat_data.risk_score > 30
    ) THEN 5
    WHEN threat_name = 'SQL Injection' AND EXISTS (
        SELECT 1 FROM threat_data 
        WHERE threat_data.threat_type = 'SQL Injection' 
        AND threat_data.risk_score > 40
    ) THEN 5
    ELSE impact
END;
