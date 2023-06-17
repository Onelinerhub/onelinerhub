# How do I use the PostgreSQL quote_ident function?
// plain

The PostgreSQL `quote_ident` function is used to escape the names of identifiers (e.g. table names, column names) that may contain special characters or keywords. It takes a single string as an argument and returns a new string with the identifier properly escaped.

For example,

```
SELECT quote_ident('column name');
```

will return:

```
"column name"
```

The parts of the code are as follows:

- `SELECT`: This is the SQL statement used to retrieve data from a database.
- `quote_ident()`: This is the PostgreSQL function used to escape the names of identifiers.
- `'column name'`: This is the string that is passed as an argument to the `quote_ident` function.

## Helpful links

- [PostgreSQL Documentation: quote_ident](https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-SQL)

onelinerhub: [How do I use the PostgreSQL quote_ident function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-quote-ident-function)