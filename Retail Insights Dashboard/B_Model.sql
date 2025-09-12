CREATE DATABASE IF NOT EXISTS B_MODEL;
USE B_MODEL;
CREATE TABLE raw_store_data(
row_id INT,
order_id VARCHAR(20),
order_date VARCHAR(20),
ship_date VARCHAR(20),
ship_mode VARCHAR(30),
customer_id VARCHAR(20),
customer_name VARCHAR(100),
segment VARCHAR(20),
country VARCHAR(50),
city VARCHAR(100),
state VARCHAR(50),
postal_code INT,
region VARCHAR(20),
product_id VARCHAR(30),
category VARCHAR(50),
sub_category VARCHAR(50),
product_name VARCHAR(200),
sales DECIMAL(10,2),
quantity INT,
discount DECIMAL(4,3),
profit DECIMAL(10,4)
);

-- Mysql import wizard to import table data from csv file.
select* from raw_store_data;


-- CUSTOMER TABLE.
CREATE TABLE customers(
customer_id varchar(30) PRIMARY KEY,
customer_name varchar(100) NOT NULL,
segment varchar(20) NOT NULL
);


-- LOCATION TABLE.
CREATE TABLE locations(
location_id INT auto_increment primary key,
country varchar(50)not null,
state varchar(50)not null,
city varchar(100) NOT NULL,
postal_code INT,
region varchar(20)NOT NULL,UNIQUE KEY 
unique_location(country,state,city,postal_code)
);


-- PRODUCTS TABLE.
CREATE TABLE products(
product_id VARCHAR(30) NOT NULL,
product_name VARCHAR(200)NOT NULL,
category VARCHAR(50)NOT NULL,
sub_category VARCHAR(50)NOT NULL,
PRIMARY KEY(product_id,product_name),
INDEX idx_product_id(product_id)
);


-- ORDERS TABLE.
CREATE TABLE orders(
order_id VARCHAR(20) PRIMARY KEY,
customer_id VARCHAR(20)NOT NULL,
location_id INT NOT NULL,
order_date DATE NOT NULL,
ship_date DATE NOT NULL,
ship_mode VARCHAR(30) NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
FOREIGN KEY (location_id) REFERENCES locations(location_id)
);




-- ORDERS_ITEMS TABLE.(Junction Table)
CREATE TABLE order_items(
row_id INT PRIMARY KEY,
order_id VARCHAR(20) NOT NULL,
product_id VARCHAR(30)NOT NULL,
product_name VARCHAR(200)NOT NULL,
quantity INT NOT NULL,
sales DECIMAL(10,2) NOT NULL,
discount DECIMAL(4,3) NOT NULL,
profit DECIMAL(10,4)NOT NULL,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id,product_name)
 REFERENCES products(product_id, product_name)
);


-- INSERT VALUES IN TABLES

-- INSERT DATA INTO CUSTOMERS TABLE.
INSERT INTO customers(customer_id,customer_name,segment) 
SELECT DISTINCT customer_id,customer_name,segment 
FROM raw_store_data;


-- INSERT DATA INTO LOCATIONS  TABLE.
INSERT INTO locations(country,state,city,postal_code,region)
SELECT DISTINCT country,state,city,postal_code,region
FROM raw_store_data;


-- INSERT DATA INTO PRODUCTS TABLE.
INSERT INTO products(product_id,product_name,category,sub_category)
SELECT DISTINCT product_id,product_name,category,sub_category
FROM raw_store_data;
SHOW COLUMNS FROM raw_store_data;


-- INSERT DATA INTO ORDERS TABLE.
INSERT INTO orders(order_id,customer_id,location_id,order_date,
ship_date,ship_mode)
SELECT DISTINCT 
r.order_id,
r.customer_id,
l.location_id,
STR_TO_DATE(r.order_date,'%m/%d/%y'),
STR_TO_DATE(r.ship_date, '%m/%d/%y'),
r.ship_mode
FROM raw_store_data r JOIN locations l 
ON(r.country = l.country AND r.state = l.state AND 
r.city = l.city AND r.postal_code  = l.postal_code
);

-- INSERT DATA INTO ORDERS ITEMS TABLE.
INSERT INTO order_items(row_id,order_id,product_id,
product_name,quantity,sales,discount,profit)
SELECT 
    row_id,
    order_id,
    product_id,
    product_name,
    quantity,
    sales,
    discount,
    profit
FROM raw_store_data;

-- Verification insertion correctness
SELECT 'customers' as table_name, COUNT(*) as row_count FROM customers
UNION ALL
SELECT 'locations', COUNT(*) FROM locations
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items;


-- Verification query to ensure no data loss
SELECT COUNT(*) as reconstructed_rows
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN locations l ON o.location_id = l.location_id
JOIN products p ON (oi.product_id = p.product_id 
                   AND oi.product_name = p.product_name);
                   
SELECT 
    (SELECT COUNT(*) FROM raw_store_data) * 21 as original_data_points,
    (SELECT COUNT(*) FROM customers) * 3 + 
    (SELECT COUNT(*) FROM locations) * 6 + 
    (SELECT COUNT(*) FROM products) * 4 + 
    (SELECT COUNT(*) FROM orders) * 6 + 
    (SELECT COUNT(*) FROM order_items) * 8 as normalized_data_points,
    ROUND(
        (1 - ((SELECT COUNT(*) FROM customers) * 3 + 
              (SELECT COUNT(*) FROM locations) * 6 + 
              (SELECT COUNT(*) FROM products) * 4 + 
              (SELECT COUNT(*) FROM orders) * 6 + 
              (SELECT COUNT(*) FROM order_items) * 8) / 209874.0
        ) * 100, 2
    ) as storage_reduction_percentage;                   
                                  




