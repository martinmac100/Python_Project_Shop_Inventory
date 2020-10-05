DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    model VARCHAR(255),
    description VARCHAR(255),
    colour VARCHAR(255),
    buy_price FLOAT,
    sell_price FLOAT,
    quantity INT,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
)
