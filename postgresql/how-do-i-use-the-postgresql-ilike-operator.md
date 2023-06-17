# How do I use the PostgreSQL ILIKE operator?
// plain

The PostgreSQL ILIKE operator is used to perform case-insensitive pattern matching. It is similar to the LIKE operator, but performs a case-insensitive search.

## Example code

```
SELECT *
FROM table_name
WHERE column_name ILIKE '%string%';
```

## Output example

```
column_name
------------
String
string
STRING
```

## Code explanation

- SELECT *: selects all columns from the table.
- FROM table_name: specifies the table from which the columns are selected.
- WHERE column_name ILIKE '%string%': searches for the string in the specified column, regardless of case. The '%' is a wildcard character that matches any characters before or after the string.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/9.1/functions-matching.html)
- [W3Schools - PostgreSQL LIKE Clause](https://www.w3schools.com/sql/sql_like.asp)

onelinerhub: [How do I use the PostgreSQL ILIKE operator?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-ilike-operator)