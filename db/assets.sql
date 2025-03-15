CREATE TABLE assets (
  id SERIAL PRIMARY KEY,           
  name VARCHAR(255) NOT NULL,        
  category VARCHAR(50) CHECK (category IN ('Hardware', 'Software', 'Data', 'People', 'Process')), 
  description TEXT                  
);


INSERT INTO assets (id, name, category, description) VALUES
(1, 'Web Server', 'Hardware', 'A physical server hosting the company website'),
(2, 'Router', 'Hardware', 'Network router for managing internet traffic'),
(3, 'E-commerce Platform', 'Software', 'Web application for online shopping'),
(4, 'Content Management System (CMS)', 'Software', 'Software used to manage and publish content on the website'),
(5, 'MySQL Database', 'Software', 'Database system for storing transactional and user data'),
(6, 'Customer Records', 'Data', 'A database containing personal and transaction data of customers'),
(7, 'Transaction Logs', 'Data', 'Logs of financial transactions processed on the website'),
(8, 'User Credentials', 'Data', 'Securely stored usernames, passwords, and authentication tokens'),
(9, 'Employee', 'People', 'A staff member responsible for managing the IT infrastructure'),
(10, 'Customer', 'People', 'End-users who interact with the website and make purchases'),
(11, 'Network Administrator', 'People', 'IT staff responsible for maintaining the network and server infrastructure'),
(12, 'Payment Processing', 'Process', 'Process of handling online payments securely through different gateways'),
(13, 'Account Authentication', 'Process', 'Authentication process to verify users during login'),
(14, 'Backups', 'Process', 'Regular system and database backups for disaster recovery');


