# How do I use the PostgreSQL NVL function?
// plain

The PostgreSQL NVL function is used to replace a NULL value with an alternate value. This is useful in cases where you want to avoid errors caused by NULL values. The syntax for the NVL function is as follows:

```
NVL(expression1, expression2)
```

where `expression1` is the expression to check for NULL values, and `expression2` is the value to replace the NULL value with. For example:

```
SELECT NVL(NULL, 'foo');
```

This will return `foo` as the output.

The NVL function can also be used with numerical values. For example:

```
SELECT NVL(NULL, 0);
```

This will return `0` as the output.

You can also use the NVL function with other expressions. For example:

```
SELECT NVL(NULL, 5 + 6);
```

This will return `11` as the output.

The NVL function is a useful tool for replacing NULL values in PostgreSQL.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/functions-conditional.html#FUNCTIONS-NVL-COALESCE-IFNULL)
- [w3resource](https://www.w3resource.com/PostgreSQL/nvl-function.php)

onelinerhub: [How do I use the PostgreSQL NVL function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-nvl-function)