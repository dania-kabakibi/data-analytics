/*
a) Table actor includes (actor_id, first_name, last_name, last_update)
b) Table film includes (film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update)
c) Table film_actor contains columns for both actor_id and film_id
d) Table rental includes (rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update), this information hard to read because it's all IDs and dates.
e) Table inventory includes (inventory_id, film_id, store_id, last_update), this information also hard to read because it's IDs and last_update date.
f) I need the film, inventory, and rental tables to determine the names of all films rented on a specific date. These tables are related through a series of one-to-many relationships. The film table has film_id as a primary key, which is referenced as a foreign key in the inventory table. The inventory table has inventory_id as a primary key, which is referenced as a foreign key in the rental table.
*/

SELECT film_id, title FROM film;
SELECT inventory_id, film_id FROM inventory;
SELECT rental_date, inventory_id FROM rental;