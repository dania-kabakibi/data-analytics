USE northwind;

/* 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a 
second query to find the name of the product that has that price. */
SELECT UnitPrice AS 'Cheapest_item'
FROM products
ORDER BY UnitPrice ASC
LIMIT 1;

SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC
LIMIT 1;

/* 2. Write a query to find the average price of all items that Northwind sells. 
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help 
using the ROUND function to round the average price to the nearest cent.) */
-- SELECT SUM(UnitPrice) AS 'Sum_of_all_prices',
-- 	COUNT(ProductID) AS 'items_number',
--  SUM(UnitPrice) / COUNT(ProductID) AS 'Average_price'
-- FROM products;

SELECT ROUND(AVG(UnitPrice), 2) AS 'Average_price'
FROM products;

/* 3. Write a query to find the price of the most expensive item that Northwind sells. Then 
write a second query to find the name of the product with that price, plus the name of 
the supplier for that product.*/
SELECT UnitPrice AS 'Most_expensive_item'
FROM products
-- ORDER BY UnitPrice DESC
-- LIMIT 1;
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

SELECT p.ProductName, s.CompanyName
FROM products p
JOIN suppliers s
USING (SupplierID)
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM products);

/* 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly 
salaries).*/
SELECT SUM(Salary) AS 'Total_monthly_payroll'
FROM employees;

/* 5. Write a query to identify the highest salary and the lowest salary amounts which any 
employee makes. (Just the amounts, not the specific employees!) */
SELECT MAX(Salary) AS 'Highest_salary',
	MIN(Salary) AS 'Lowest_salary'
FROM employees;

/* 6. Write a query to find the name and supplier ID of each supplier and the number of 
items they supply. Hint: Join is your friend here.*/
SELECT s.SupplierID,
	s.CompanyName,
    COUNT(ProductID) AS 'Number_of_items'
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

/* 7. Write a query to find the list of all category names and the average price for items 
in each category.*/
SELECT c.CategoryName, AVG(p.UnitPrice) AS 'Average_price'
FROM categories c
JOIN products p
USING (CategoryID)
GROUP BY c.CategoryName;

/* 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, 
what is the name of each supplier and the number of items they supply.*/
SELECT s.CompanyName AS 'Supplier_name',
	COUNT(p.ProductID) AS 'Items_number'
FROM suppliers s
JOIN products p
USING (SupplierID)
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

/* 9. Write a query to list products currently in inventory by the product id, product name, 
and inventory value (calculated by multiplying unit price by the number of units on 
hand). Sort the results in descending order by value. If two or more have the same 
value, order by product name. If a product is not in stock, leave it off the list. */
SELECT ProductID, ProductName, 
	UnitPrice * UnitsInStock AS 'Inventory_value'
FROM products
WHERE UnitsInStock > 0
ORDER BY Inventory_value DESC, ProductName;