CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, description) VALUES
    ('Item 1', 'First sample item'),
    ('Item 2', 'Second sample item'),
    ('Item 3', 'Third sample item');