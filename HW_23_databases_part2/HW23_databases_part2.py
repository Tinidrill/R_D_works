# TABLES CREATING
#import sqlite3
# db = sqlite3.connect("book_store.sqlite")
# curr = db.cursor()
#cursor.execute()
# users = ("CREATE TABLE IF NOT EXISTS users ("
#                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                "first_name TEXT,"
#                "last_name TEXT,"
#                "age INTEGER NOT NULL)"
#                "FOREIGN KEY (id) REFERENCES purchase(user_id)")
#           )
#
# purchase = ("CREATE TABLE IF NOT EXISTS purchase ("
#                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                "user_id INTEGER NOT NULL,"
#                "book_id INTEGER NOT NULL"
#                )"
#                )
# publishing_houses = ("CREATE TABLE IF NOT EXISTS publishing_houses ("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                 "name TEXT,"
#                 "rating DEFAULT 5,"
#                 "FOREIGN KEY (id) REFERENCES books(publishing_house_id)")
#                 )
# books = ("CREATE TABLE IF NOT EXISTS books ("
#                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                "title TEXT,"
#                "author TEXT,"
#                "year INTEGER NOT NULL"
#                "price INTEGER NOT NULL"
#                "publishing_house_id INTEGER NOT NULL"
#                "FOREIGN KEY (id) REFERENCES purchase(book_id)")
#                )"
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
-- SELECT COUNT(purchase.book_id) AS purchase_number, books.author
-- FROM books
-- LEFT JOIN purchase ON purchase.book_id = books.id
-- GROUP BY books.author

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
