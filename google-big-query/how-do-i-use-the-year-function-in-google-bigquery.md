# How do I use the YEAR function in Google BigQuery?
// plain

The YEAR function in Google BigQuery is used to extract the year from a date or timestamp expression. It takes in one parameter, which is a date or timestamp expression. The output of the YEAR function is an integer between 1 and 9999.

For example:
```
SELECT YEAR('2015-06-13') as year;
```
The output of this query will be:
```
year
2015
```

The parts of the code are:
- `SELECT`: This is a keyword used to indicate that a query is being executed
- `YEAR('2015-06-13')`: This is the YEAR function, taking in the date '2015-06-13' as a parameter
- `as year`: This is an alias for the output of the query, which will be stored in the column 'year'

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [YEAR Function Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#date-and-time-functions)

onelinerhub: [How do I use the YEAR function in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-the-year-function-in-google-bigquery)