# 3rd TASK
# RESULT
# The table 'users1" is created. The names can't be empty.
# 5 users were added - empty fields are not allowed


CREATE TABLE users1
(
    id         INTEGER
        PRIMARY KEY AUTOINCREMENT ,
    First_name TEXT NOT NULL,
    Last_name  TEXT NOT NULL,
    Age        INTEGER
);