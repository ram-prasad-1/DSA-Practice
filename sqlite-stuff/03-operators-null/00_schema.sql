-- Sample store schema shared by all files in this folder.
-- Rebuild (or reset) the db with:
--   sqlite3 play.db < 00_schema.sql

PRAGMA foreign_keys = ON;

DROP VIEW IF EXISTS order_totals;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE customers (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT NOT NULL UNIQUE,
    city        TEXT,
    country     TEXT NOT NULL,
    signed_up   DATE NOT NULL,
    referred_by INTEGER REFERENCES customers(id)   -- NULL = found us themselves
);

CREATE TABLE products (
    id          INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES categories(id),
    name        TEXT NOT NULL,
    price       REAL NOT NULL CHECK (price >= 0),
    in_stock    INTEGER NOT NULL DEFAULT 0,
    discount    REAL                               -- NULL = not decided; 0 = decided, none
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    placed_at   DATE NOT NULL,
    status      TEXT NOT NULL CHECK (status IN ('pending','shipped','delivered','cancelled'))
);

CREATE TABLE order_items (
    order_id   INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity   INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_placed_at ON orders(placed_at);
CREATE INDEX idx_products_category ON products(category_id);

CREATE VIEW order_totals AS
SELECT o.id            AS order_id,
       o.customer_id,
       o.placed_at,
       o.status,
       SUM(oi.quantity * oi.unit_price) AS total
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id;

INSERT INTO categories (id, name) VALUES
    (1, 'Keyboards'),
    (2, 'Mice'),
    (3, 'Monitors'),
    (4, 'Audio'),
    (5, 'Cables');

INSERT INTO customers (id, name, email, city, country, signed_up, referred_by) VALUES
    (1, 'Ada Lovelace',    'ada@example.com',     'London',    'UK',      '2024-01-15', NULL),
    (2, 'Grace Hopper',    'grace@example.com',   'New York',  'USA',     '2024-02-03', NULL),
    (3, 'Alan Turing',     'alan@example.com',    'Manchester','UK',      '2024-02-20', 1),
    (4, 'Katherine Johnson','katherine@example.com','Hampton', 'USA',     '2024-03-11', 2),
    (5, 'Linus Torvalds',  'linus@example.com',   NULL,        'Finland', '2024-04-02', NULL),
    (6, 'Margaret Hamilton','margaret@example.com','Boston',   'USA',     '2024-05-19', 2),
    (7, 'Yukihiro Matsumoto','matz@example.com',  'Matsue',    'Japan',   '2024-06-08', NULL),
    (8, 'Barbara Liskov',  'barbara@example.com', NULL,        'USA',     '2024-07-24', 4);

INSERT INTO products (id, category_id, name, price, in_stock, discount) VALUES
    (1,  1, 'Mechanical Keyboard 87-key',  129.00, 42,  0.10),
    (2,  1, 'Low-profile Wireless Board',   89.50, 17,  NULL),
    (3,  1, 'Split Ergonomic Keyboard',    249.00,  5,  0),
    (4,  2, 'Wireless Mouse',               39.99, 120, 0.05),
    (5,  2, 'Trackball Mouse',              64.00,   8, NULL),
    (6,  2, 'Vertical Ergo Mouse',          74.25,   0, NULL),
    (7,  3, '27" 4K Monitor',              399.00,  11, 0.15),
    (8,  3, '34" Ultrawide Monitor',       749.00,   3, 0),
    (9,  4, 'USB Condenser Mic',           119.00,  26, NULL),
    (10, 4, 'Noise-cancelling Headphones', 299.00,  14, 0.20),
    (11, 5, 'USB-C Cable 2m',                9.99, 500, NULL),
    (12, 5, 'HDMI 2.1 Cable',               14.50, 210, 0.05),
    (13, 5, 'Thunderbolt 4 Cable',          49.00,   0, NULL);

INSERT INTO orders (id, customer_id, placed_at, status) VALUES
    (1001, 1, '2024-03-01', 'delivered'),
    (1002, 2, '2024-03-04', 'delivered'),
    (1003, 1, '2024-04-12', 'shipped'),
    (1004, 3, '2024-04-18', 'cancelled'),
    (1005, 4, '2024-05-02', 'delivered'),
    (1006, 5, '2024-05-21', 'delivered'),
    (1007, 2, '2024-06-09', 'shipped'),
    (1008, 6, '2024-06-30', 'pending'),
    (1009, 7, '2024-07-14', 'delivered'),
    (1010, 1, '2024-08-01', 'pending'),
    (1011, 4, '2024-08-15', 'shipped'),
    (1012, 5, '2024-09-02', 'delivered');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (1001, 1,  1, 129.00),
    (1001, 4,  2,  39.99),
    (1001, 11, 3,   9.99),
    (1002, 7,  1, 399.00),
    (1002, 12, 1,  14.50),
    (1003, 3,  1, 249.00),
    (1003, 5,  1,  64.00),
    (1004, 8,  1, 749.00),
    (1005, 10, 1, 299.00),
    (1005, 9,  1, 119.00),
    (1005, 11, 2,   9.99),
    (1006, 2,  2,  89.50),
    (1006, 4,  1,  39.99),
    (1007, 8,  1, 749.00),
    (1007, 13, 2,  49.00),
    (1008, 6,  1,  74.25),
    (1009, 1,  2, 129.00),
    (1009, 10, 1, 299.00),
    (1010, 12, 4,  14.50),
    (1011, 7,  2, 399.00),
    (1011, 9,  1, 119.00),
    (1012, 3,  1, 249.00),
    (1012, 11, 5,   9.99),
    (1012, 4,  1,  39.99);
