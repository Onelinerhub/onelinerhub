# How do I use the PostgreSQL UNNEST function?
// plain

The PostgreSQL UNNEST function allows you to expand an array into a set of rows. It takes an array as an input and returns a set of rows containing the elements of the array.

For example, if you have an array `arr` containing the elements `[1, 2, 3]`, the following code will return three rows, each containing one element of the array:

```
SELECT unnest(arr)
FROM (SELECT ARRAY[1, 2, 3] AS arr) AS t;

unnest
-------
1
2
3
(3 rows)
```

The code above consists of two parts:

1. The `SELECT` statement, which uses the `UNNEST` function to expand the array `arr` into a set of rows.
2. The `FROM` clause, which defines the array `arr` as `ARRAY[1, 2, 3]`.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-array.html#ARRAY-FUNCTIONS-TABLE).

onelinerhub: [How do I use the PostgreSQL UNNEST function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-unnest-function)