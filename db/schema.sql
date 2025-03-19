CREATE TABLE assets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(50),
  description TEXT
);

CREATE TABLE threats (
  id SERIAL PRIMARY KEY,
  asset_id INT REFERENCES assets(id),
  threat_name VARCHAR(255) NOT NULL,
  description TEXT,
  risk_level INT CHECK (risk_level BETWEEN 1 AND 10)
);

CREATE TABLE vulnerabilities (
  id SERIAL PRIMARY KEY,
  vulnerability_name VARCHAR(255) NOT NULL,
  vulnerable_asset_id INT REFERENCES assets(id),
  threat_id INT REFERENCES threats(id), 
  description TEXT, 
  risk_level INT CHECK (risk_level BETWEEN 1 AND 10)
);

CREATE TABLE risk_ratings (
  id SERIAL PRIMARY KEY,
  vulnerability_id INT REFERENCES vulnerabilities(id),
  asset_id INT REFERENCES assets(id),
  threat_id INT REFERENCES threats(id),
  risk_level INT CHECK (risk_level BETWEEN 1 AND 10)
  );
