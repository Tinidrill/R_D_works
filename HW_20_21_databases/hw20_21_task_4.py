# 4th TASK
# RESULT
# The table 'users2" is created with one column FULL_NAME
# to avoid duplicates in Name-Last name combinations
# 5 users were added. Duplicates of names were not allowed.

CREATE TABLE users2
(
    id        INTEGER
        PRIMARY KEY AUTOINCREMENT,
    Full_name TEXT
        UNIQUE ,
    Age       INTEGER NOT NULL
);

INSERT INTO users2 (Full_name, Age)
VALUES ('Svitlana Kohut', 22),
    ('Yana Kohut', 18),
    ('Anna Kohut', 16),
    ('LIna Kohut', 10),
    ('Matt Mes', 25);