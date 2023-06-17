# How can I extract the year from a date in PostgreSQL?
// plain

To extract the year from a date in PostgreSQL, you can use the `EXTRACT` function.

## Example code

```
SELECT EXTRACT(YEAR FROM '2020-01-01'::DATE);
```

## Output example

```
2020
```

The code above uses the `EXTRACT` function to extract the year from the date `2020-01-01`. The `YEAR` keyword is used to specify the type of data to extract from the date.

## Code explanation

- `SELECT`: Used to query the database
- `EXTRACT`: Function used to extract data from a date
- `YEAR`: Keyword used to specify the type of data to extract from the date
- `2020-01-01`: Date used in the example

## Helpful links
- [PostgreSQL Documentation - EXTRACT](https://www.postgresql.org/docs/9.1/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT)

onelinerhub: [How can I extract the year from a date in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-extract-the-year-from-a-date-in-postgresql)