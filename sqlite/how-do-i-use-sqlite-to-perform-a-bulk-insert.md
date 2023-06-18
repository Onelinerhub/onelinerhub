# How do I use SQLite to perform a bulk insert?
// plain

To perform a bulk insert using SQLite, you can use the `INSERT INTO` statement with the `SELECT` statement. This allows you to quickly insert multiple rows into a table.

For example, the following code block inserts all rows from the `users` table into the `backup_users` table:
```
INSERT INTO backup_users
SELECT * FROM users;
```

The code block above consists of two parts:
1. `INSERT INTO backup_users` - This statement will insert the data into the `backup_users` table.
2. `SELECT * FROM users` - This statement will select all rows from the `users` table.

For more information, you can refer to the [SQLite documentation](https://www.sqlite.org/lang_insert.html).

onelinerhub: [How do I use SQLite to perform a bulk insert?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-to-perform-a-bulk-insert)