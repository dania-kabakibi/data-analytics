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
