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

-- Day3 Example 1:
SELECT o.OrderID, c.CompanyName AS 'Customer', o.OrderDate
FROM Orders o
JOIN customers c ON o.CustomerID = c.CustomerID
ORDER BY o.OrderDate DESC
LIMIT 5;

-- Day3 Example 2:
SELECT o.OrderID, c.CompanyName AS 'Customer', o.OrderDate
FROM Orders o
JOIN customers c USING (CustomerID)
ORDER BY o.OrderDate DESC
LIMIT 5;

-- Day3 Example 3:
SELECT p.ProductName, c.CategoryName , p.UnitPrice
FROM products p
INNER JOIN categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

SELECT p.ProductName, c.CategoryName , p.UnitPrice
FROM products p
INNER JOIN categories c USING (CategoryID)
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

-- Day3 Example 4:
SELECT o.OrderID,
	c.CompanyName,
    SUM(od.Quantity * od.UnitPrice) AS 'Order Total'
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
INNER JOIN `order details` od ON o.OrderID = od.OrderID
GROUP BY o.OrderID, c.CompanyName
ORDER BY 'Order Total' DESC
LIMIT 5;

-- Day3 Example 5:
SELECT c.CompanyName,
	COUNT(o.OrderID) AS 'Order Count'
FROM customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY 'Order Count' ASC
LIMIT 5;

-- Day4 Example 1:
SELECT COUNT(OrderID) AS 'Total Orders'
FROM orders;

-- Day4 Example 2:
SELECT SUM(Freight) AS 'Total Freight',
	AVG(Freight) AS 'Average Freight', 
    MIN(Freight) AS 'Minimun Freight', 
    MAX(Freight) AS 'Maximum Freight'
FROM orders;

-- Day4 Example 4:
SELECT COUNT(DISTINCT Country) AS 'Countries Served'
FROM Customers;