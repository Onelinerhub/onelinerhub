# functions

How do I use PostgreSQL year functions?
// plain

PostgreSQL includes a variety of functions for working with dates and times. The most common of these are the YEAR functions, which allow you to extract the year from a date or timestamp.

The syntax for these functions is `YEAR(date)` or `YEAR(timestamp)`. For example, to extract the year from a date:

```
SELECT YEAR('2020-10-20');
```

## Output example

```
2020
```

This code will return the year from the given date.

The YEAR functions can also be used to extract the year from a timestamp. For example:

```
SELECT YEAR(TIMESTAMP '2020-10-20 11:30:00');
```

## Output example

```
2020
```

This code will return the year from the given timestamp.

For more information on PostgreSQL date and time functions, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-datetime.html).

onelinerhub: [functions

How do I use PostgreSQL year functions?](https://onelinerhub.com/postgresql/functions--how-do-i-use-postgresql-year-functions)