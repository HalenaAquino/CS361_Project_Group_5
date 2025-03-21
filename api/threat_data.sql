CREATE TABLE threat_data (
    id SERIAL PRIMARY KEY,
    source TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    data JSONB NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
