# How do I use Google Big Query date functions?
// plain

Google Big Query date functions allow you to manipulate and analyze date and time values. Here is an example of how to use the `DATE_DIFF` function to calculate the difference between two dates:

```
SELECT DATE_DIFF(TIMESTAMP('2020-01-01'), TIMESTAMP('2019-12-31'), DAY) AS days_difference
```

This would output:
```
days_difference
1
```

The code consists of the following parts:

1. `SELECT` - This keyword is used to indicate that the statement is a query.
2. `DATE_DIFF` - This is the date function used to calculate the difference between two dates.
3. `TIMESTAMP('2020-01-01')` - This is the first timestamp argument used to calculate the difference.
4. `TIMESTAMP('2019-12-31')` - This is the second timestamp argument used to calculate the difference.
5. `DAY` - This is the unit of time used to calculate the difference.
6. `AS days_difference` - This is used to assign the result of the calculation to a column named `days_difference`.

For more information on Big Query date functions, please refer to the [Big Query Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#date-and-time-functions).

onelinerhub: [How do I use Google Big Query date functions?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-date-functions)