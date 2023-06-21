-- TASK 2

-- SELECT purchase.id, purchase.date, users.first_name, users.last_name
-- FROM purchase
-- INNER JOIN users ON purchase.user_id = users.id

--TASK 3

-- SELECT users.id, users.first_name, users.last_name, books.title
-- FROM purchase
-- LEFT JOIN books ON purchase.book_id = books.id
-- LEFT JOIN users ON purchase.user_id = users.id
-- ORDER BY users.id

-- TASK 4.1

-- SELECT users.id, users.first_name, users.last_name, SUM(books.price)
-- AS total_purchase
-- FROM purchase
-- LEFT JOIN books ON purchase.book_id = books.id
-- LEFT JOIN users ON purchase.user_id = users.id
-- GROUP BY users.id

--TASK 4.2

-- SELECT users.id, users.first_name, users.last_name, COUNT(purchase.id)
-- AS purchase_count
-- FROM purchase
-- LEFT JOIN books ON purchase.book_id = books.id
-- LEFT JOIN users ON purchase.user_id = users.id
-- GROUP BY users.id

-- TASK 4.3 - I don't know how to sort out one author only

SELECT
    COUNT(p.id) AS amount
FROM purchases p
JOIN books b ON b.id = p.book_id
WHERE b.author = 'Rowling';

-- TASK 4.4

-- SELECT books.author, SUM(books.price), COUNT(purchase.id)
-- FROM purchase
-- LEFT JOIN books ON purchase.book_id = books.id
-- GROUP BY books.author

-- TASK 4.5 - not working completely correct

-- SELECT books.title, COUNT(purchase.id) AS purchase_number
-- FROM purchase
-- LEFT JOIN books ON purchase.book_id = books.id
-- HAVING purchase_number