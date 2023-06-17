# query

How do I write a PostgreSQL delete query?
// plain

A PostgreSQL delete query is used to delete data from a table in a PostgreSQL database. It is important to note that the delete query will permanently remove all the data from the table.

The syntax of a PostgreSQL delete query is as follows:

```
DELETE FROM table_name
WHERE condition;
```

Where `table_name` is the name of the table from which data is to be deleted and `condition` is the condition which must be satisfied in order for the data to be deleted.

For example, to delete all rows from the table `employees` where the `salary` is less than 10000, the query would be:

```
DELETE FROM employees
WHERE salary < 10000;
```

The output of this query would be the number of rows deleted.

The parts of the delete query are as follows:

* `DELETE FROM`: This is the keyword used to indicate that a delete query is being executed.
* `table_name`: This is the name of the table from which data is to be deleted.
* `WHERE`: This is the keyword used to indicate the condition which must be satisfied in order for the data to be deleted.
* `condition`: This is the condition which must be satisfied in order for the data to be deleted.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/9.5/sql-delete.html).

onelinerhub: [query

How do I write a PostgreSQL delete query?](https://onelinerhub.com/postgresql/query--how-do-i-write-a-postgresql-delete-query)