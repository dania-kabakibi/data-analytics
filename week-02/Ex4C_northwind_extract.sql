/*
a) The name of the table that holds the items Northwind sells is products
b) The name of the table that holds the types/categories of the items Northwind sells is categories
*/

SELECT * FROM employees;
-- Margaret Peacock is the employee whose name look like she's a bird.

SELECT * FROM products;
-- My query returns 77 records
-- I changed my query to retrieve only 10 rows, by choose Limit to 10 rows
-- BONUS: SELECT * FROM products LIMIT 10; I remember my instructor Deodat metioned LIMIT during the class

SELECT * FROM categories;
-- The categoryID of Seafood is 8

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders;