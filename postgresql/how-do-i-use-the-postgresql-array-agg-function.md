# How do I use the PostgreSQL array_agg function?
// plain

The PostgreSQL `array_agg` function is used to aggregate values from a group of rows into a single array. It takes an expression as an argument and returns an array containing all the values from the group.

## Example


```
SELECT array_agg(name)
FROM users
```

## Output example
 `{'John', 'Mary', 'James'}`

This example returns an array containing the `name` values from the `users` table.

## Code explanation


* `SELECT` - specifies the columns to be selected
* `array_agg` - the PostgreSQL array_agg function
* `name` - the expression to be aggregated into an array
* `FROM users` - specifies the table from which to select the values

## Helpful links

* [PostgreSQL Documentation: array_agg](https://www.postgresql.org/docs/9.4/functions-aggregate.html#FUNCTIONS-AGGREGATE-TABLE-ARRAY)

onelinerhub: [How do I use the PostgreSQL array_agg function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-array-agg-function)