DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    model VARCHAR(255),
    description VARCHAR(255),
    colour VARCHAR(255),
    buy_price FLOAT,
    sell_price FLOAT
);

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255)

);
