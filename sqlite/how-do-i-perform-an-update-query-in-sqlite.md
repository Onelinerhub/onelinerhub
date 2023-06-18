# How do I perform an update query in SQLite?
// plain

An update query in SQLite can be used to modify existing data in a table. The basic syntax of an update query is as follows:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

In this example, `table_name` is the name of the table in which the data is being updated, `column1`, `column2`, etc. are the names of the columns being updated, and `value1`, `value2`, etc. are the new values being assigned to those columns. The `WHERE` clause specifies the condition that must be met for the update to take place.

For example, the following query will update the `name` and `age` columns of the `users` table for all users whose `id` is `1`:

```
UPDATE users
SET name = 'John Doe', age = 30
WHERE id = 1;
```

This query will result in the following output:

```
Query OK, 1 row affected (0.01 sec)
```

The following parts compose the query above:

* `UPDATE users` - this specifies the table to be updated
* `SET name = 'John Doe', age = 30` - this sets the new values for the specified columns
* `WHERE id = 1` - this specifies the condition that must be met for the update to take place

For more information, see the [SQLite documentation](https://www.sqlite.org/lang_update.html).

onelinerhub: [How do I perform an update query in SQLite?](https://onelinerhub.com/sqlite/how-do-i-perform-an-update-query-in-sqlite)