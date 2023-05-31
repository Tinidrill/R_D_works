import sqlite3

conn = sqlite3.connect("database_1.sqlite")
cursor = conn.cursor()

# from console

--SELECT * FROM users;
--SELECT * FROM users WHERE age > 30;
--SELECT age, COUNT(age) as users FROM users WHERE age > 30 GROUP BY age;
--SELECT age, COUNT(age) as users FROM users WHERE age > 30 GROUP BY age ORDER BY users DESC;
--SELECT age, COUNT(age) as users FROM users WHERE age > 30 GROUP BY age HAVING users > 1 ORDER BY users DESC;
