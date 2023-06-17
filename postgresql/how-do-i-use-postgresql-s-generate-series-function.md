# How do I use PostgreSQL's generate_series function?
// plain

The `generate_series` function in PostgreSQL is used to generate a set of numbers within a specified range. It can be used in various ways to generate a series of numbers, dates, or timestamps.

## Example code


```
SELECT * FROM generate_series(1, 10);
```

## Output example

```
 generate_series
----------------
               1
               2
               3
               4
               5
               6
               7
               8
               9
              10
(10 rows)
```

This example code will generate a series of numbers from 1 to 10. The `generate_series` function takes two parameters - the starting and ending values. The code above can be modified to generate a series of dates or timestamps as well.

For example, to generate a series of dates from 2020-01-01 to 2020-01-10, the code would be:

```
SELECT * FROM generate_series('2020-01-01'::date, '2020-01-10'::date, '1 day'::interval);
```

## Output example

```
    generate_series
---------------------
 2020-01-01 00:00:00
 2020-01-02 00:00:00
 2020-01-03 00:00:00
 2020-01-04 00:00:00
 2020-01-05 00:00:00
 2020-01-06 00:00:00
 2020-01-07 00:00:00
 2020-01-08 00:00:00
 2020-01-09 00:00:00
 2020-01-10 00:00:00
(10 rows)
```

The `generate_series` function can also be used to generate a series of timestamps with an interval. For example, to generate a series of timestamps from 2020-01-01 00:00:00 to 2020-01-01 01:00:00 with a 15 minute interval, the code would be:

```
SELECT * FROM generate_series('2020-01-01 00:00:00'::timestamp,
                             '2020-01-01 01:00:00'::timestamp,
                             '15 minutes'::interval);
```

## Output example

```
      generate_series
--------------------------
 2020-01-01 00:00:00+00
 2020-01-01 00:15:00+00
 2020-01-01 00:30:00+00
 2020-01-01 00:45:00+00
 2020-01-01 01:00:00+00
(5 rows)
```

## Helpful links

- [PostgreSQL Documentation - generate_series](https://www.postgresql.org/docs/9.1/functions-srf.html#FUNCTIONS-SRF-GENERATE-SERIES)

onelinerhub: [How do I use PostgreSQL's generate_series function?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-generate-series-function)