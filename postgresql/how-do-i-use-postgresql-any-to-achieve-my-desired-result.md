# How do I use PostgreSQL ANY to achieve my desired result?
// plain

PostgreSQL ANY is a comparison operator that is used to compare a value to any value in a list or results from a subquery. It returns true if the comparison is true for any of the values in the list or subquery.

For example, if we wanted to find all the records in a table where the value of the column `name` is equal to any of the values in a list, we could use the following query:

```
SELECT *
FROM table_name
WHERE name = ANY (ARRAY['John', 'Mary', 'Jane']);
```

This query would return all the records in the table where the value of the column `name` is equal to either `John`, `Mary` or `Jane`.

## Code explanation


1. `SELECT *` - This is the clause used to select all the columns from the table.
2. `FROM table_name` - This is the clause used to specify which table the query should be run on.
3. `WHERE name = ANY (ARRAY['John', 'Mary', 'Jane'])` - This is the clause used to specify the condition for the query. It compares the value of the column `name` to any of the values in the array `['John', 'Mary', 'Jane']`.

## Helpful links

- [PostgreSQL Documentation - ANY](https://www.postgresql.org/docs/9.1/functions-comparisons.html)

onelinerhub: [How do I use PostgreSQL ANY to achieve my desired result?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-any-to-achieve-my-desired-result)