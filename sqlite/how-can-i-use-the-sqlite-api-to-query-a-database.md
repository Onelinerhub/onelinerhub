# How can I use the SQLite API to query a database?
// plain

The SQLite API can be used to query a database by executing SQL statements. For example, the following code block can be used to query a database table called `users` and retrieve the name of each user:

```
SELECT name FROM users;
```
This will return a list of names, for example:
```
John
Jane
Bob
```

The following parts are used in the code above:
- `SELECT`: This is an SQL keyword which specifies the data to be retrieved.
- `name`: This is the column name in the `users` table which contains the name of the users.
- `FROM users`: This specifies the table from which the data should be retrieved.

For more information on using the SQLite API to query a database, please refer to the [SQLite documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How can I use the SQLite API to query a database?](https://onelinerhub.com/sqlite/how-can-i-use-the-sqlite-api-to-query-a-database)