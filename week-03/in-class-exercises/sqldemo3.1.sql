-- Dania Kabakibi
-- April 20, 2026
-- the Northwind Database

USE northwind;
SHOW TABLES;
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'northwind'
AND table_type = 'BASE TABLE';

-- Example 1:
SELECT ProductName, UnitPrice 
FROM products;

-- Example 2:
SELECT * 
FROM products;

-- Example 3:
SELECT ProductName AS 'Product', 
UnitPrice AS 'Price(USD)',
UnitsInStock AS 'Stock'
FROM products;

-- Example 4:
SELECT CompanyName, City, Country
FROM customers
WHERE Country = 'Germany';

-- Example 5:
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice > 50;

-- Example 6:
SELECT OrderID, CustomerID, ShipCountry, Freight
FROM orders
WHERE ShipCountry = 'France';

-- Example 7:
SELECT ProductName, UnitsInStock, ReorderLevel
FROM products
WHERE UnitsInStock < ReorderLevel;

-- Example 8:
SELECT OrderID, Freight
FROM orders
WHERE Freight >= 100;

-- Example 10:
SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitPrice > 20 AND UnitsInStock > 50;

-- Example 11:
SELECT CompanyName, Country
FROM customers
WHERE Country = 'UK' OR 'Ireland';

-- Example 12:
SELECT ProductName, CategoryID, UnitPrice
FROM products
WHERE (CategoryID = 1 OR CategoryID = 2) 
AND UnitPrice < 20;

-- Example 13:
SELECT CompanyName, Country
FROM customers
WHERE Country != 'U.S.A';

-- Example 14:
SELECT ProductName
FROM products
WHERE NOT discontinued = 1;

-- Example 15:
SELECT CompanyName, Country
FROM customers
WHERE Country IN ('France', 'Germany', 'Spain');

-- Example 16:
SELECT ProductName, SupplierID
FROM products
WHERE SupplierID NOT IN (1 , 2, 3);

-- Example 17:
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice BETWEEN 10 AND 20;

-- Example 19:
SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS NULL;

-- Example 20:
SELECT FirstName, LastName, Region
FROM employees
WHERE Region IS NOT NULL;

-- Example 24:
SELECT OrderID, CustomerID, OrderDate
FROM orders
WHERE OrderDate = '1997-01-01';

-- Example 26:
SELECT OrderID, OrderDate
FROM orders
WHERE YEAR(OrderDate) = 1997 AND MONTH(OrderDate) = 6;

-- Example 27:
SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice DESC;

-- Example 28:
SELECT CompanyName, Country, City
FROM customers
ORDER BY Country ASC, CompanyName ASC;

-- Example 29:
SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice DESC
LIMIT 5;

-- Example 30:
SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice DESC
LIMIT 5, 5;

-- Example 31:
SELECT DISTINCT Country
FROM customers
ORDER BY Country;

-- Example 32:
SELECT DISTINCT Country, City
FROM customers
ORDER BY Country, City;

-- Eample 33:
SELECT CONCAT(FirstName, ' ', LastName) AS 'Full Name', Title
FROM employees;

-- Example 36:
SELECT ProductName, 
	UnitPrice AS 'Original_Price', 
	UnitPrice * 0.9 AS '10% Discount_Price'
FROM products;
