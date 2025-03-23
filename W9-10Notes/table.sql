CREATE TABLE IF NOT EXISTS ITEMS (
    item_name VARCHAR(20) PRIMARY KEY,
    count NUMERIC NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);