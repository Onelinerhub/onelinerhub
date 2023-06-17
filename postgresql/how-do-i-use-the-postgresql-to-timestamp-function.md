# How do I use the PostgreSQL to_timestamp function?
// plain

The PostgreSQL `to_timestamp` function is used to convert a string to a timestamp. It takes two arguments: a string and a format mask. The format mask is used to specify the format of the string that is being converted.

For example:

```
SELECT to_timestamp('2020-10-20 10:30', 'YYYY-MM-DD HH24:MI');

```

## Output example

```
2020-10-20 10:30:00
```

## Code explanation


* `to_timestamp` - the PostgreSQL function used to convert a string to a timestamp
* `'2020-10-20 10:30'` - the string to be converted
* `'YYYY-MM-DD HH24:MI'` - the format mask used to specify the format of the string

More information can be found in the [PostgreSQL documentation](https://www.postgresql.org/docs/9.1/functions-formatting.html).

onelinerhub: [How do I use the PostgreSQL to_timestamp function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-to-timestamp-function)