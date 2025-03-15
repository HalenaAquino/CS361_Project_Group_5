CREATE TABLE tva_mapping (
id SERIAL PRIMARY KEY,
asset_id INT REFERENCES assets(id),
threat_name VARCHAR(255),
vulnerability_description TEXT,
likelihood INT CHECK (likelihood BETWEEN 1 AND 5),
impact INT CHECK (impact BETWEEN 1 AND 5),
risk_score INT GENERATED ALWAYS AS (likelihood * impact) STORED
);

INSERT INTO tva_mapping (id, asset_id, threat_name, vulnerability_description, likelihood, impact) VALUES
(1, 1, "DDoS Attack", "An attacker could flood the servers with a series with of requests; causing the server to slow down or crash completely", 4, 2),
(2, 9, "Employee has a lack of education in Information Security", "An employee could accidentally introduce threats into the company system via Phishing", 3, 4),
(3, 1, "Physical breach", "An attacker could physically break into the company's server room and destroy equipment or intoduce malware into the web server", 1, 5),
(4, 3, "SQL Injection", "An attacker could insert malicious SQL code into the e-commerce platform", 4, 5),
(5, 8, "Insecurely stored passwords and user credentials", "Weak passwords or unsafely stores login information can be easily obtained and used by an attacker to access the company's systems", 3, 4),
(6, 12, "Lack of account authentication (MFA)", "Without proper account authentication, such as MFA, an attacker could easily access employee accounts", 3, 4),
(7, 14, "Lack of backups to company systems", "Outdated systems and databases are more at risk to an attack", 2, 4),
(8, 3, "E-commerce platform going down", "If the e-commerce platform were to go down, the company would lose business and creditability", 3, 3),
(9, 9, "Employee lack of training/mistakes", "If an employee is not properly trained for their job or makes some kind of mistake, they could harm the company's system", 3, 3),
(10, 12, "Payment processing platform going down", "If the e-commerce platform were to go down, the company would lose money and creditability", 3, 3),
(11, 9, "Excessive privileges for job", "An employee could have more access or privileges than is needed for their job, so if their account were to be accessed by an attacker, it would be more detrimental", 4, 5),
(12, 6, "Weak encryption of customer records", "If customer records lacked the proper encryption, they would be easier for an attacker to steal", 3, 3),
(13, 2, "Outdated firmware", "Outdated firmware would make the router more vulnerable to attacks", 3, 4),
(14, 4, "Website defacement", "An attacker would deface the company's website, resulting in the business losing creditability", 3, 1),
(15, 6, "Data leak", "Customer data could be leaked, making the company look bad, or possibly causing legal trouble", 3, 4),
(16, 2, "Man in the Middle Attack", "An attacker could intercept and possibly alter communications between employees", 2, 4);
