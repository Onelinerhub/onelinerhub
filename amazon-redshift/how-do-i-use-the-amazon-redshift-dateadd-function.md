# How do I use the Amazon Redshift Dateadd function?
// plain

The `DATEADD` function in Amazon Redshift is used to add or subtract a specified time interval from a given date. It takes three parameters: an interval type, a number, and a date.

```
SELECT DATEADD(day, 10, '2018-12-25');
```

## Output example
 `2018-01-04`

This example adds 10 days to the date `2018-12-25` and returns the result `2018-01-04`.

The interval type is one of the following: `year`, `quarter`, `month`, `day`, `hour`, `minute`, `second`, `millisecond`.

The number is the number of interval types to add or subtract.

The date is the date to which the interval is added or subtracted.

## Helpful links

- [Amazon Redshift Documentation - DATEADD](https://docs.aws.amazon.com/redshift/latest/dg/r_DATEADD_function.html)
- [PostgreSQL Documentation - DATEADD](https://www.postgresql.org/docs/9.1/functions-datetime.html#FUNCTIONS-DATETIME-ADD-SUBTR)

onelinerhub: [How do I use the Amazon Redshift Dateadd function?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-dateadd-function)