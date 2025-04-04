CREATE DATABASE pingpong;
USE pingpong;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    qr_code VARCHAR(50) UNIQUE,
    rfid_tag VARCHAR(50) UNIQUE,
    membership_status ENUM('active', 'inactive') DEFAULT 'active'
);

CREATE TABLE access_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    entry_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
