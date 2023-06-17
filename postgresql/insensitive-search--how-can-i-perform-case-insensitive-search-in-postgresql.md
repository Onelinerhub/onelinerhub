# insensitive search

How can I perform case insensitive search in PostgreSQL?
// plain

To perform a case insensitive search in PostgreSQL, you can use the `ILIKE` operator. This operator is similar to the `LIKE` operator, but is not case sensitive.

For example, the following code block can be used to search for the string 'hello' in the 'my_table' table, regardless of case:

```
SELECT * FROM my_table WHERE name ILIKE '%hello%';
```

The output of this code would be a list of all records in the 'my_table' table that contain the string 'hello', regardless of case.

## Code explanation


- `SELECT *`: This is the keyword used to select all columns from the table.
- `FROM my_table`: This specifies which table the query should be performed on.
- `WHERE name ILIKE '%hello%'`: This is the condition that is used to perform the case insensitive search. The `ILIKE` operator is used instead of the `LIKE` operator to make the search case insensitive. The `%` characters are used as wildcards to match any characters before and after the string 'hello'.

## Helpful links

- [PostgreSQL Documentation - LIKE Clause](https://www.postgresql.org/docs/current/sql-expressions.html#SQL-SYNTAX-MATCHING)
- [PostgreSQL Documentation - ILIKE Clause](https://www.postgresql.org/docs/current/sql-expressions.html#SQL-SYNTAX-MATCHING-SIMILAR)

onelinerhub: [insensitive search

How can I perform case insensitive search in PostgreSQL?](https://onelinerhub.com/postgresql/insensitive-search--how-can-i-perform-case-insensitive-search-in-postgresql)