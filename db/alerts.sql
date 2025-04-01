-- Create alerts table for logging notification events
CREATE TABLE IF NOT EXISTS alert_logs (
    alert_id SERIAL PRIMARY KEY,
    threat_name VARCHAR(255) NOT NULL,
    risk_score INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    alert_message TEXT NOT NULL,
    recipient_email VARCHAR(255),
    notification_type VARCHAR(50) NOT NULL,  -- 'email', 'webhook', etc.
    status VARCHAR(50) NOT NULL,  -- 'sent', 'failed', 'pending'
    error_message TEXT,
    webhook_url VARCHAR(255),
    response_code INTEGER,
    response_message TEXT
);

-- Index for faster searches by date range
CREATE INDEX idx_alert_timestamp ON alert_logs(timestamp);

-- Index for filtering by threat type
CREATE INDEX idx_alert_threat ON alert_logs(threat_name);

-- Index for filtering by risk score (for reports on high-risk alerts)
CREATE INDEX idx_alert_risk ON alert_logs(risk_score);

-- Create a view for high-risk alerts (risk score > 20)
CREATE VIEW high_risk_alerts AS
SELECT * FROM alert_logs
WHERE risk_score > 20
ORDER BY timestamp DESC;
