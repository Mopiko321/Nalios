-- Ex 4: PSQL
-- - Write pseudo-SQL statements to create database tables to store the products of a basic
-- webshop. Each product has a name, a price, a creation date and may belong to several
-- categories. Categories have a name and a flag to indicate whether the category is
-- private or public.

-- - Write a SQL query to find the list of products that belong to more than 5 public categories


----------------------------------------------------------
-- I suppose everything is done with the user postgres
----------------------------------------------------------

create database basic_webshop;

-- To connect to the database, use:
-- \c basic_webshop;

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_private BOOLEAN NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    creation_date TIMESTAMP NOT NULL
);
-- Create a many-to-many relationship between products and categories with junction table
CREATE TABLE product_categories (
    product_id INT REFERENCES products(id),
    category_id INT REFERENCES categories(id),
    PRIMARY KEY (product_id, category_id)
);

-- Inserting test data into categories 
INSERT INTO categories (name, is_private) VALUES
('Electronics', FALSE),
('Books', FALSE),
('Clothing', TRUE),
('Home & Garden', FALSE),
('Toys', FALSE),
('Sports', TRUE),
('Health & Beauty', FALSE),
('Gaming', FALSE),
('Music', FALSE),
('Office', FALSE);

-- Insert test data into products
INSERT INTO products (name, price, creation_date) VALUES
('Smartphone', 699.99, '2023-01-15 10:00:00'),
('Laptop', 1299.99, '2023-02-20 12:30:00'),
('T-Shirt', 19.99, '2023-03-05 14:45:00'),
('Coffee Maker', 49.99, '2023-04-10 09:15:00'),
('Action Figure', 24.99, '2023-05-25 11:00:00'),
('Yoga Mat', 29.99, '2023-06-30 08:30:00'),
('Super Gadget', 199.99, '2023-07-15 15:00:00');

-- Insert test data into product_categories
INSERT INTO product_categories (product_id, category_id) VALUES
(1, 1), -- Smartphone in Electronics
(1, 4), -- Smartphone in Home & Garden
(2, 1), -- Laptop in Electronics
(2, 5), -- Laptop in Toys
(3, 2), -- T-Shirt in Books
(3, 6), -- T-Shirt in Sports
(4, 4), -- Coffee Maker in Home & Garden
(5, 5), -- Action Figure in Toys
(6, 7),-- Yoga Mat in Health & Beauty
(6, 1), -- Yoga Mat in Electronics
(6, 2), -- Yoga Mat in Books
(6, 3), -- Yoga Mat in Clothing
(6, 4), -- Yoga Mat in Home & Garden
(6, 5), -- Yoga Mat in Toys
(7, 1),  -- Electronics
(7, 2),  -- Books
(7, 4),  -- Home & Garden
(7, 5),  -- Toys
(7, 7),  -- Health & Beauty
(7, 8),  -- Gaming
(7, 9),  -- Music
(7, 10); -- Office



-- Query to find products that belong to more than 5 public categories
SELECT p.id, p.name, COUNT(pc.category_id) AS category_count
FROM products p
JOIN product_categories pc ON p.id = pc.product_id
JOIN categories c ON pc.category_id = c.id
WHERE c.is_private = FALSE
GROUP BY p.id, p.name
HAVING COUNT(pc.category_id) > 5;