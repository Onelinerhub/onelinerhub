# How can I use the NOT EQUAL operator in PostgreSQL?
// plain

The NOT EQUAL operator in PostgreSQL is used to compare two values and return a boolean value based on whether or not the values are equal. The operator is written as `!=` and is used in a `WHERE` clause to filter results.

For example, the following query will return all rows from the `users` table where the `name` column does not equal `John`:

```sql
SELECT * FROM users WHERE name != 'John';
```

The code above consists of the following parts:
1. `SELECT *` - This part of the query selects all columns from the `users` table.
2. `FROM users` - This part of the query specifies the table from which the data should be retrieved.
3. `WHERE name != 'John'` - This part of the query uses the NOT EQUAL operator to filter the results and only return rows where the `name` column does not equal `John`.

For more information on the NOT EQUAL operator in PostgreSQL, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/9.2/functions-comparisons.html).

onelinerhub: [How can I use the NOT EQUAL operator in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-use-the-not-equal-operator-in-postgresql)