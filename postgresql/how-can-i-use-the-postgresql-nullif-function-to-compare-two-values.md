# How can I use the PostgreSQL NULLIF function to compare two values?
// plain

The PostgreSQL NULLIF function can be used to compare two values and return a null value if the values are equal. Here is an example of how it can be used:

```
SELECT NULLIF(1, 1);
```

This will return `NULL` since the two values being compared are equal.

The syntax for the NULLIF function is as follows:

```
NULLIF(value1, value2)
```

- `value1` is the first value to compare.
- `value2` is the second value to compare.

If `value1` and `value2` are equal, the NULLIF function will return `NULL`. Otherwise, it will return `value1`.

Here is another example of using the NULLIF function:

```
SELECT NULLIF(1, 2);
```

This will return `1` since the two values being compared are not equal.

## Helpful links
- [PostgreSQL Documentation - NULLIF](https://www.postgresql.org/docs/9.1/functions-comparison.html#FUNCTIONS-COMPARISON-NULLIF)

onelinerhub: [How can I use the PostgreSQL NULLIF function to compare two values?](https://onelinerhub.com/postgresql/how-can-i-use-the-postgresql-nullif-function-to-compare-two-values)