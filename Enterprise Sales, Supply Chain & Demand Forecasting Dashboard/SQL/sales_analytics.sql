-- Create Database Tables

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    region VARCHAR(50),
    market VARCHAR(50)
);

CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    sub_category VARCHAR(100)
);

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    sales NUMERIC(12,2),
    quantity INT,
    discount NUMERIC(5,2),
    profit NUMERIC(12,2),
    shipping_cost NUMERIC(12,2),

    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

----------------------------------------------------
-- Revenue by Market
----------------------------------------------------

SELECT
    c.market,
    ROUND(SUM(o.sales),2) AS total_revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.market
ORDER BY total_revenue DESC;

----------------------------------------------------
-- Profit by Category
----------------------------------------------------

SELECT
    p.category,
    ROUND(SUM(o.profit),2) AS total_profit
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;

----------------------------------------------------
-- Top 10 Customers
----------------------------------------------------

SELECT
    c.customer_name,
    ROUND(SUM(o.sales),2) AS revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 10;

----------------------------------------------------
-- Monthly Sales Trend
----------------------------------------------------

SELECT
    DATE_TRUNC('month', order_date) AS month,
    ROUND(SUM(sales),2) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

----------------------------------------------------
-- Shipping Cost Analysis
----------------------------------------------------

SELECT
    ship_mode,
    ROUND(AVG(shipping_cost),2) AS avg_shipping_cost,
    ROUND(SUM(shipping_cost),2) AS total_shipping_cost
FROM orders
GROUP BY ship_mode;

----------------------------------------------------
-- Delivery Performance
----------------------------------------------------

SELECT
    ship_mode,
    ROUND(AVG(ship_date - order_date),2) AS avg_delivery_days
FROM orders
GROUP BY ship_mode;

----------------------------------------------------
-- Profit Margin by Category
----------------------------------------------------

SELECT
    p.category,
    ROUND((SUM(o.profit) / SUM(o.sales))*100,2) AS profit_margin
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category;

----------------------------------------------------
-- Forecast Dataset Preparation
----------------------------------------------------

SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales) AS revenue,
    SUM(quantity) AS units_sold,
    SUM(profit) AS profit
FROM orders
GROUP BY month
ORDER BY month;