CREATE TABLE incident_logs (
    id SERIAL PRIMARY KEY,
    threat_name VARCHAR(255) NOT NULL,
    response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) CHECK (status IN ('Detected', 'In Progress', 'Resolved')) NOT NULL
);
