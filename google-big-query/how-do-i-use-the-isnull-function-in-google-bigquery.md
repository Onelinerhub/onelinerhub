# How do I use the ISNULL function in Google BigQuery?
// plain

The ISNULL function in Google BigQuery is used to check if a value is null. It returns true if a value is null and false if a value is not null.

## Example code

```
SELECT ISNULL(null_value) as is_null
FROM `project.dataset.table`
```
## Output example

```
+----------+
| is_null  |
+----------+
| true     |
+----------+
```

The code above checks if the value of the column `null_value` is null and returns true if it is.

The code consists of the following parts:
- `SELECT`: specifies the columns to be returned
- `ISNULL(null_value)`: checks if the value of the column `null_value` is null
- `as is_null`: gives the column a name
- `FROM`: specifies the table from which the data should be retrieved

For more information on the ISNULL function, please refer to the official BigQuery documentation: https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#isnull-function

onelinerhub: [How do I use the ISNULL function in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-the-isnull-function-in-google-bigquery)