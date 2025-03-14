CREATE TABLE assets (
  id SERIAL PRIMARY KEY,           
  name VARCHAR(255) NOT NULL,        
  category VARCHAR(50) CHECK (category IN ('Hardware', 'Software', 'Data', 'People', 'Process')), 
  description TEXT                  
);


INSERT INTO assets (name, category, description) VALUES
('Web Server', 'Hardware', 'A physical server hosting the company website'),
('Router', 'Hardware', 'Network router for managing internet traffic'),
('E-commerce Platform', 'Software', 'Web application for online shopping'),
('Content Management System (CMS)', 'Software', 'Software used to manage and publish content on the website'),
('MySQL Database', 'Software', 'Database system for storing transactional and user data'),
('Customer Records', 'Data', 'A database containing personal and transaction data of customers'),
('Transaction Logs', 'Data', 'Logs of financial transactions processed on the website'),
('User Credentials', 'Data', 'Securely stored usernames, passwords, and authentication tokens'),
('Employee', 'People', 'A staff member responsible for managing the IT infrastructure'),
('Customer', 'People', 'End-users who interact with the website and make purchases'),
('Network Administrator', 'People', 'IT staff responsible for maintaining the network and server infrastructure'),
('Payment Processing', 'Process', 'Process of handling online payments securely through different gateways'),
('Account Authentication', 'Process', 'Authentication process to verify users during login'),
('Backups', 'Process', 'Regular system and database backups for disaster recovery');


