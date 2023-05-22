# Done in SQL console - copied here
# RESULT
#   created table with the name 'users'
#   added 5 users via SQL interface
#   added the same 5 users via console
#   10 users (allowed duplicates) are in the table 'users'

CREATE TABLE users
(
    id         INTEGER
        PRIMARY KEY AUTOINCREMENT,
    First_name TEXT,
    Last_name  TEXT,
    Age        INTEGER
);
INSERT INTO users (First_name, Last_name, Age)
VALUES ('Svitlana', 'Kohut', 20),
    ('Yana', 'Kohut', 18),
    ('Ana', 'Kohut', 16),
    ('Lina', 'Kohut', 10),
    ('Matt', 'Mes', 22);
