CREATE DATABASE threat_intel;

USE threat_intel;

CREATE TABLE threat_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source VARCHAR(50) NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    data JSON NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
