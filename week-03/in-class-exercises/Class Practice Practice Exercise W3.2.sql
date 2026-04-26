USE northwind;

/* 1- Task: Write a query to list ProductID, ProductName, UnitPrice, and UnitsInStock from the 
Products table. Order the results by UnitPrice from highest to lowest. 
Hint: Use the ORDER BY clause with DESC to sort in descending order.*/
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM products
ORDER BY UnitPrice DESC;

/* 2- Task: Write a query to list all customers. Order them first by Country (A–Z), then by 
CompanyName (A–Z) within each country. 
Hint: You can list multiple columns in the ORDER BY clause separated by commas.*/
SELECT CustomerID, CompanyName, ContactName, Country
FROM customers
ORDER BY Country ASC, CompanyName ASC;

/* 3- Task: Write a query that counts the total number of products in each category. Display the 
CategoryID and the count, labeling the count ProductCount. Order the results so the category 
with the most products appears first. 
Hint: Use COUNT() with GROUP BY on CategoryID, then ORDER BY the count descending.*/
SELECT CategoryID, COUNT(ProductID) AS 'ProductCount'
FROM products
GROUP BY CategoryID
ORDER BY ProductCount DESC;

/* 4- Task: Write a query against the Order Details table that calculates the total revenue per order. 
Total revenue for a line is UnitPrice × Quantity × (1 − Discount). Label the total Revenue and 
display it alongside OrderID. Order the results by Revenue from largest to smallest. 
Hint: Use SUM() on the calculated expression and GROUP BY OrderID.*/
SELECT OrderID, 
	ROUND(SUM(UnitPrice * Quantity * (1 - Discount)), 2) AS 'Revenue'
FROM `order details`
GROUP BY OrderID
ORDER BY Revenue DESC;

/* 5- Task: Write a query to list the number of orders placed by each employee. Show EmployeeID 
and label the count OrderCount. Only include employees who have handled more than 50 
orders. Order by OrderCount, largest first. 
Hint: Use GROUP BY EmployeeID, then filter groups with HAVING instead of WHERE.*/
SELECT EmployeeID, COUNT(OrderID) AS 'OrderCount'
FROM orders
GROUP BY EmployeeID
HAVING COUNT(OrderID) > 50
ORDER BY OrderCount DESC;

/* 6- Task: Write a query that lists each shipper (ShipVia) and counts the number of orders assigned 
to them. Label the count OrderCount. Order results by ShipperID ascending. 
Hint: Use GROUP BY on the ShipVia column in the Orders table. */
SELECT ShipVia,
	COUNT(OrderID) AS 'OrderCount'
FROM orders
GROUP BY ShipVia
ORDER BY ShipVia ASC;

/* 7- Task: List every product together with the name of its category. Display ProductID, 
ProductName, and CategoryName. Order alphabetically by CategoryName, then by 
ProductName within each category. 
Hint: Join the Products table to the Categories table on the CategoryID column.*/
SELECT p.ProductID, p.ProductName, c.CategoryName
FROM products p
JOIN categories c
USING (CategoryID)
ORDER BY c.CategoryName ASC, p.ProductName ASC;

/* 8- Task: Write a query that shows each order and the company name of the customer who placed 
it. Display OrderID, OrderDate, and CompanyName. Order by OrderDate from most recent to 
oldest. 
Hint: Join the Orders table to the Customers table on CustomerID.*/
SELECT o.OrderID, o.OrderDate, c.CompanyName
FROM orders o
JOIN customers c
USING (CustomerID)
ORDER BY o.OrderDate DESC;

/* 9- Task: Write a query that calculates the average unit price of products in each category. Display 
CategoryName and the average price labeled AvgPrice, rounded to 2 decimal places. Only show 
categories where the average price is greater than $20. Order by AvgPrice descending. 
Hint: Join Products and Categories, use AVG() with GROUP BY CategoryID, filter with HAVING, 
and use ROUND().*/
SELECT c.CategoryName, 
	ROUND(AVG(p.UnitPrice), 2) AS 'AvgPrice'
FROM products p
JOIN categories c
USING (CategoryID)
GROUP BY c.CategoryName
HAVING AVG(p.UnitPrice) > 20
ORDER BY AvgPrice DESC;

/* 10- Task: Write a query that lists each employee's full name along with the total number of orders 
they have processed. Show FullName (combined FirstName + LastName) and OrderCount. Only 
include employees who have processed at least 70 orders. Order by OrderCount descending, 
then by FullName ascending. 
Hint: Join Employees and Orders on EmployeeID, aggregate with COUNT and GROUP BY, then 
filter with HAVING.*/
SELECT e.EmployeeID,
	CONCAT(e.FirstName, ' ', e.LastName) AS 'FullName', 
	COUNT(o.OrderID) AS 'OrderCount'
FROM employees e
JOIN orders o
USING (EmployeeID)
GROUP BY EmployeeID, FullName
HAVING OrderCount >= 70
ORDER BY OrderCount DESC, FullName ASC;