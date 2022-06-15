DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

-- CREATE TABLE users (
--   id SERIAL PRIMARY KEY,
--   first_name VARCHAR(255),
--   last_name VARCHAR(255)
-- );

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    item VARCHAR(255)
);

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions(
  id SERIAL PRIMARY KEY,
  amount DECIMAL(18,2),
  merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
  date DATE 
  tag_id INT REFERENCES tags(id) ON DELETE CASCADE
);


