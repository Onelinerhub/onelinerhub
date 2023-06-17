# How do I use the PostgreSQL string_agg function?
// plain

The `string_agg` function in PostgreSQL is used to concatenate strings from a group of rows into a single string. It takes two arguments - a string expression and an order by clause. The string expression is the value that will be concatenated together. The order by clause is used to specify the order in which the strings should be concatenated.

For example, to concatenate a list of names in alphabetical order, the following code could be used:

```
SELECT string_agg(name, ', ' ORDER BY name)
FROM people;
```

This would return a string of names, separated by commas, in alphabetical order:

```
John, Mary, Paul
```

The code consists of the following parts:

- `SELECT`: this indicates that a query is being executed.
- `string_agg`: this is the function that will be used to concatenate the strings.
- `name`: this is the string expression that will be concatenated.
- `ORDER BY name`: this is the order by clause that specifies the ordering of the strings.

For more information on the `string_agg` function, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-aggregate.html#FUNCTIONS-AGG-STRING-TABLE).

onelinerhub: [How do I use the PostgreSQL string_agg function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-string-agg-function)