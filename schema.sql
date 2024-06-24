-- schema.sql

-- Create Date Dimension Table
CREATE TABLE Date (
    date_id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE,
    year INT,
    month INT,
    day INT
);

-- Create Company Dimension Table
CREATE TABLE Company (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    stock_id VARCHAR(10),
    company_name VARCHAR(100),
    sector VARCHAR(50),
    industry VARCHAR(50)
);

-- Create StockPrices Fact Table
CREATE TABLE StockPrices (
    stock_id VARCHAR(10),
    date_id INT,
    open_price DECIMAL(10, 2),
    close_price DECIMAL(10, 2),
    high_price DECIMAL(10, 2),
    low_price DECIMAL(10, 2),
    volume INT,
    PRIMARY KEY (stock_id, date_id),
    FOREIGN KEY (date_id) REFERENCES Date(date_id)
);
