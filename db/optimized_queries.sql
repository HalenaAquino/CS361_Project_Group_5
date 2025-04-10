-- Optimize SQL Queries
-- Create indexes on frequently queried columns
CREATE INDEX idx_threat_type ON threat_data(threat_type);
CREATE INDEX idx_risk_score ON threat_data(risk_score);

-- Optimize a common query by using indexed fields
SELECT threat_type, COUNT(*) AS occurrence
FROM threat_data
WHERE risk_score > 10
GROUP BY threat_type
ORDER BY occurrence DESC;

-- Database Backup Procedure
-- Create a backup of the database
BACKUP DATABASE threat_intelligence_db
TO DISK = '/backups/threat_intelligence_db.bak'
WITH FORMAT, MEDIANAME = 'ThreatDB_Backup', NAME = 'Full Backup';

-- Restore Database from Backup
-- Ensure the database is not in use before restoring
RESTORE DATABASE threat_intelligence_db
FROM DISK = '/backups/threat_intelligence_db.bak'
WITH REPLACE;
