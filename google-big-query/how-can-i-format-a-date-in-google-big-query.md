# How can I format a date in Google Big Query?
// plain

Google Big Query supports the Standard SQL dialect and provides a `DATE_FORMAT` function to format dates. The function takes two arguments: the date to format and the format string. The format string uses the same syntax as the `strftime` function in the C language.

```
SELECT DATE_FORMAT(CURRENT_DATE(), '%Y-%m-%d')
```

## Output example

```
2020-07-01
```

The code above will format the current date in the format `YYYY-MM-DD`.

The parts of the code are:
- `SELECT`: This is a SQL keyword to indicate that the query will return a result.
- `DATE_FORMAT`: This is the function that formats the date.
- `CURRENT_DATE()`: This is a built-in function that returns the current date.
- `%Y-%m-%d`: This is the format string to output the date in the format `YYYY-MM-DD`.

For more information on formatting dates in Google Big Query, see the [documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#date_format).

onelinerhub: [How can I format a date in Google Big Query?](https://onelinerhub.com/google-big-query/how-can-i-format-a-date-in-google-big-query)