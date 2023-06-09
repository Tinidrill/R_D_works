# TASK 1 - CREATION OF THE TABLES

# import sqlite3
#
# db = sqlite3.connect("book_store.sqlite")
# curr = db.cursor()

# table_users = ("CREATE TABLE IF NOT EXISTS users ("
#                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                "first_name TEXT,"
#                "last_name TEXT,"
#                "age INTEGER NOT NULL,"
#                FOREIGN KEY (id) REFERENCES purchase(user_id))"
#                )
#
#
# table_publishing_houses = ("CREATE TABLE IF NOT EXISTS publishing_houses ("
#                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                "rating DEFAULT 5,"
#                "name TEXT,"
#                "FOREIGN KEY (id) REFERENCES books(publishing_house_id))"
#                )
#
# table_purchase = ("CREATE TABLE IF NOT EXISTS payback ("
#                  "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                  "user_id INTEGER NOT NULL,"
#                  "book_id INTEGER NOT NULL,"
#                  "date TEXT DEFAULT CURRENT_TIMESTAMP,"
#                  )
#
# table_books = ("CREATE TABLE IF NOT EXISTS books ("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                 "title TEXT,"
#                 "author TEXT,"
#                 "year INTEGER NOT NULL,"
#                 "price INTEGER NOT NULL,"
#                 "publishing_house_id INTEGER NOT NULL,"
#                 FOREIGN KEY (id) REFERENCES purchase(book_id))"
#                 )
#
# curr.execute(table_users)
# curr.execute(table_publishing_house)
# curr.execute(table_purchase)
# curr.execute(table_books)