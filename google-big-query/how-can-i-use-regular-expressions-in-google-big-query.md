# How can I use regular expressions in Google Big Query?
// plain

Regular expressions can be used in Google Big Query to search for specific patterns in data. For example, the following code block can be used to search for a pattern of the form `[A-Z]{2}[0-9]{3}` in a table called `my_table`.

```
SELECT * FROM my_table
WHERE REGEXP_CONTAINS(my_column, r'[A-Z]{2}[0-9]{3}')
```

The code block will return all records from the table where the value in the `my_column` column matches the regular expression pattern.

The parts of the code are as follows:

- `SELECT * FROM my_table`: This statement selects all columns and records from the `my_table` table.
- `WHERE REGEXP_CONTAINS(my_column, r'[A-Z]{2}[0-9]{3}')`: This statement filters the results to only include records where the value in the `my_column` column matches the regular expression pattern `[A-Z]{2}[0-9]{3}`.

For more information about using regular expressions in Big Query, see the [Big Query documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#regexp_contains).

onelinerhub: [How can I use regular expressions in Google Big Query?](https://onelinerhub.com/google-big-query/how-can-i-use-regular-expressions-in-google-big-query)