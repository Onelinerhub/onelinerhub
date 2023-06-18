# How do I use SQLite keywords to query a database?
// plain

To query a database using SQLite keywords, you can use the `SELECT` statement. This statement is used to retrieve data from a table in the database. For example, the following code will select all rows from the table `users`:

```SQL
SELECT * FROM users;
```

The output of this statement will be a list of all the rows in the `users` table.

You can also use the `WHERE` clause to filter the results of the query. For example, the following code will select all rows from the `users` table where the `age` column is greater than 18:

```SQL
SELECT * FROM users WHERE age > 18;
```

The output of this statement will be a list of all the rows in the `users` table that have an age greater than 18.

You can also use the `ORDER BY` clause to sort the results of the query. For example, the following code will select all rows from the `users` table and sort them by the `name` column in descending order:

```SQL
SELECT * FROM users ORDER BY name DESC;
```

The output of this statement will be a list of all the rows in the `users` table sorted in descending order by the `name` column.

Other SQLite keywords that can be used to query a database include `GROUP BY`, `HAVING`, `LIMIT`, and `JOIN`. For more information about these keywords and how to use them, please refer to the [SQLite documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How do I use SQLite keywords to query a database?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-keywords-to-query-a-database)