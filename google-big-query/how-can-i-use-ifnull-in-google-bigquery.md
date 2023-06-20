# How can I use IFNULL in Google BigQuery?
// plain

IFNULL is a Google BigQuery function that can be used to replace NULL values in a result set with a specified value. This is useful when working with data that contains NULL values and you want to replace them with a value of your choice.

The syntax for using the IFNULL function is as follows:

```
SELECT IFNULL(column_name, replacement_value)
FROM table_name
```

For example, if you have a table with the following data:

| id | name |
|----|------|
| 1  | John |
| 2  | NULL |

You can use the IFNULL function to replace the NULL value with a string of your choice, such as "Unknown":

```
SELECT IFNULL(name, 'Unknown')
FROM table_name
```

This will return the following result set:

| name   |
|--------|
| John   |
| Unknown|

The IFNULL function can also be used to replace NULL values in calculations. For example, if you want to calculate the average of a column that contains NULL values, you can use the IFNULL function to replace the NULL values with a value of your choice:

```
SELECT AVG(IFNULL(column_name, 0))
FROM table_name
```

This will return the average of the column with the NULL values replaced by 0.

For more information on the IFNULL function, please refer to the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#ifnull).

onelinerhub: [How can I use IFNULL in Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-use-ifnull-in-google-bigquery)