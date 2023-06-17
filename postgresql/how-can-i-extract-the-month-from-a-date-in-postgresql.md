# How can I extract the month from a date in PostgreSQL?
// plain

To extract the month from a date in PostgreSQL, you can use the `EXTRACT` function.

## Example code

```
SELECT EXTRACT(MONTH FROM '2019-03-25') AS month;
```

## Output example

```
 month
-------
     3
(1 row)
```

The `EXTRACT` function takes two parameters, the part of the date you want to extract (in this case, `MONTH`) and the date from which you want to extract it. In this example, the date is `2019-03-25`. The output of the code is the month, in this case 3.

## Code explanation

- `EXTRACT`: function to extract a part of a date
- `MONTH`: part of the date to extract
- `2019-03-25`: date from which to extract the month

## Helpful links
- [PostgreSQL EXTRACT](https://www.postgresql.org/docs/9.1/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT)

onelinerhub: [How can I extract the month from a date in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-extract-the-month-from-a-date-in-postgresql)