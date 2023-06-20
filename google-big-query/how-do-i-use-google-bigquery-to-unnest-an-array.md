# How do I use Google BigQuery to unnest an array?
// plain

Google BigQuery allows users to unnest an array by using the `UNNEST` function. The `UNNEST` function takes an array as its input and returns a table with a single row for each element in the array.

For example, the following code block will take the array `[1,2,3]` and return a table with three rows, one for each element in the array:
```
SELECT * FROM UNNEST([1,2,3])
```

## Output example

```
1
2
3
```

The code consists of two parts:
1. The `UNNEST` function, which takes the array as its input and returns a table with a single row for each element in the array.
2. The `SELECT` statement, which specifies which columns from the table returned by the `UNNEST` function should be included in the output.

For more information on the `UNNEST` function, please see the [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays).

onelinerhub: [How do I use Google BigQuery to unnest an array?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-to-unnest-an-array)