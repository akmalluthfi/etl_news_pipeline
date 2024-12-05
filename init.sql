CREATE DATABASE IF NOT EXISTS liputan6;

USE liputan6;

CREATE TABLE IF NOT EXISTS breaking_news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author VARCHAR(255),
    published_at DATE,
    text TEXT
);
