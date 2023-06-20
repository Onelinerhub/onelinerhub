# How do I calculate the difference between two dates using Google Big Query?
// plain

To calculate the difference between two dates using Google Big Query, you can use the `DATE_DIFF` function. This function takes two dates as arguments and returns the difference between them in days.

For example, the following code will return the number of days between August 1, 2020 and August 15, 2020:

```
SELECT DATE_DIFF(
  DATE '2020-08-01',
  DATE '2020-08-15',
  DAY
)
```

This will output `14` as the result.

The `DATE_DIFF` function takes three arguments:
- `date_1`: The first date to calculate the difference from.
- `date_2`: The second date to calculate the difference to.
- `unit`: The unit of time to calculate the difference in. This can be one of `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`, `MICROSECOND`, `NANOSECOND`.

## Helpful links
- [BigQuery DATE_DIFF Function Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#date_diff)

onelinerhub: [How do I calculate the difference between two dates using Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-calculate-the-difference-between-two-dates-using-google-big-query)